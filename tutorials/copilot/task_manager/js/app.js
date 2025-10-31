/**
 * Task Manager Application
 * Modern, accessible task management with local storage persistence
 */

class TaskManager {
    constructor() {
        this.tasks = [];
        this.currentFilter = 'all';
        this.taskIdCounter = 1;
        
        // DOM elements
        this.elements = {
            taskForm: document.getElementById('taskForm'),
            taskInput: document.getElementById('taskInput'),
            taskInputError: document.getElementById('taskInputError'),
            taskList: document.getElementById('taskList'),
            emptyState: document.getElementById('emptyState'),
            filterButtons: document.querySelectorAll('.filter-button'),
            clearCompletedBtn: document.getElementById('clearCompleted'),
            shortcutsHelp: document.getElementById('shortcutsHelp'),
            shortcutsModal: document.getElementById('shortcutsModal'),
            modalClose: document.querySelector('.modal-close'),
            
            // Stats elements
            totalTasks: document.getElementById('totalTasks'),
            completedTasks: document.getElementById('completedTasks'),
            pendingTasks: document.getElementById('pendingTasks')
        };
        
        this.init();
    }
    
    /**
     * Initialize the application
     */
    init() {
        this.loadTasks();
        this.bindEvents();
        this.render();
        this.updateStats();
        
        // Focus the input on load
        this.elements.taskInput.focus();
        
        console.log('Task Manager initialized successfully');
    }
    
    /**
     * Bind all event listeners
     */
    bindEvents() {
        // Form submission
        this.elements.taskForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.addTask();
        });
        
        // Input validation
        this.elements.taskInput.addEventListener('input', () => {
            this.clearError();
        });
        
        // Filter buttons
        this.elements.filterButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                this.setFilter(e.target.dataset.filter);
            });
        });
        
        // Clear completed tasks
        this.elements.clearCompletedBtn.addEventListener('click', () => {
            this.clearCompletedTasks();
        });
        
        // Modal controls
        this.elements.shortcutsHelp.addEventListener('click', () => {
            this.showModal();
        });
        
        this.elements.modalClose.addEventListener('click', () => {
            this.hideModal();
        });
        
        // Global keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            this.handleKeyboardShortcuts(e);
        });
        
        // Modal backdrop click
        this.elements.shortcutsModal.addEventListener('click', (e) => {
            if (e.target === this.elements.shortcutsModal) {
                this.hideModal();
            }
        });
        
        // Storage event for cross-tab synchronization
        window.addEventListener('storage', (e) => {
            if (e.key === 'taskManager_tasks') {
                this.loadTasks();
                this.render();
                this.updateStats();
            }
        });
    }
    
    /**
     * Handle keyboard shortcuts
     */
    handleKeyboardShortcuts(e) {
        // Escape key - close modal or clear input
        if (e.key === 'Escape') {
            if (this.elements.shortcutsModal.classList.contains('active')) {
                this.hideModal();
            } else if (this.elements.taskInput.value) {
                this.elements.taskInput.value = '';
                this.clearError();
            }
            return;
        }
        
        // Don't handle shortcuts when typing in input or modal is open
        if (e.target.tagName === 'INPUT' || this.elements.shortcutsModal.classList.contains('active')) {
            return;
        }
        
        switch (e.key) {
            case 'a':
            case 'A':
                e.preventDefault();
                this.elements.taskInput.focus();
                break;
                
            case '1':
                e.preventDefault();
                this.setFilter('all');
                break;
                
            case '2':
                e.preventDefault();
                this.setFilter('pending');
                break;
                
            case '3':
                e.preventDefault();
                this.setFilter('completed');
                break;
                
            case 'c':
            case 'C':
                e.preventDefault();
                this.clearCompletedTasks();
                break;
                
            case '?':
                e.preventDefault();
                this.showModal();
                break;
        }
    }
    
    /**
     * Add a new task
     */
    addTask() {
        const text = this.elements.taskInput.value.trim();
        
        if (!this.validateTaskInput(text)) {
            return;
        }
        
        const task = {
            id: this.taskIdCounter++,
            text: text,
            completed: false,
            createdAt: new Date().toISOString(),
            completedAt: null
        };
        
        this.tasks.unshift(task); // Add to beginning for newest first
        this.elements.taskInput.value = '';
        this.clearError();
        
        this.saveTasks();
        this.render();
        this.updateStats();
        
        // Announce to screen readers
        this.announceToScreenReader(`Task "${text}" added successfully`);
        
        // Focus back to input for continuous adding
        this.elements.taskInput.focus();
    }
    
    /**
     * Validate task input
     */
    validateTaskInput(text) {
        this.clearError();
        
        if (!text) {
            this.showError('Please enter a task description.');
            this.elements.taskInput.focus();
            return false;
        }
        
        if (text.length > 200) {
            this.showError('Task description must be 200 characters or less.');
            this.elements.taskInput.focus();
            return false;
        }
        
        // Check for duplicate tasks
        const duplicate = this.tasks.find(task => 
            task.text.toLowerCase() === text.toLowerCase() && !task.completed
        );
        
        if (duplicate) {
            this.showError('This task already exists in your pending list.');
            this.elements.taskInput.focus();
            return false;
        }
        
        return true;
    }
    
    /**
     * Toggle task completion status
     */
    toggleTask(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (!task) return;
        
        task.completed = !task.completed;
        task.completedAt = task.completed ? new Date().toISOString() : null;
        
        this.saveTasks();
        this.render();
        this.updateStats();
        
        // Announce to screen readers
        const status = task.completed ? 'completed' : 'marked as pending';
        this.announceToScreenReader(`Task "${task.text}" ${status}`);
    }
    
    /**
     * Delete a task
     */
    deleteTask(taskId) {
        const taskIndex = this.tasks.findIndex(t => t.id === taskId);
        if (taskIndex === -1) return;
        
        const task = this.tasks[taskIndex];
        
        // Confirm deletion for completed tasks or show immediate feedback
        if (task.completed || confirm(`Are you sure you want to delete "${task.text}"?`)) {
            this.tasks.splice(taskIndex, 1);
            
            this.saveTasks();
            this.render();
            this.updateStats();
            
            // Announce to screen readers
            this.announceToScreenReader(`Task "${task.text}" deleted`);
        }
    }
    
    /**
     * Clear all completed tasks
     */
    clearCompletedTasks() {
        const completedCount = this.tasks.filter(task => task.completed).length;
        
        if (completedCount === 0) {
            this.announceToScreenReader('No completed tasks to clear');
            return;
        }
        
        if (confirm(`Are you sure you want to delete ${completedCount} completed task${completedCount !== 1 ? 's' : ''}?`)) {
            this.tasks = this.tasks.filter(task => !task.completed);
            
            this.saveTasks();
            this.render();
            this.updateStats();
            
            this.announceToScreenReader(`${completedCount} completed task${completedCount !== 1 ? 's' : ''} cleared`);
        }
    }
    
    /**
     * Set the current filter
     */
    setFilter(filter) {
        this.currentFilter = filter;
        
        // Update active filter button
        this.elements.filterButtons.forEach(button => {
            button.classList.toggle('active', button.dataset.filter === filter);
        });
        
        this.render();
        
        // Announce filter change
        const count = this.getFilteredTasks().length;
        this.announceToScreenReader(`Showing ${count} ${filter} task${count !== 1 ? 's' : ''}`);
    }
    
    /**
     * Get filtered tasks based on current filter
     */
    getFilteredTasks() {
        switch (this.currentFilter) {
            case 'completed':
                return this.tasks.filter(task => task.completed);
            case 'pending':
                return this.tasks.filter(task => !task.completed);
            default:
                return this.tasks;
        }
    }
    
    /**
     * Render the task list
     */
    render() {
        const filteredTasks = this.getFilteredTasks();
        
        // Show/hide empty state
        this.elements.emptyState.style.display = filteredTasks.length === 0 ? 'flex' : 'none';
        
        // Clear existing tasks
        this.elements.taskList.innerHTML = '';
        
        // Render tasks
        filteredTasks.forEach(task => {
            const taskElement = this.createTaskElement(task);
            this.elements.taskList.appendChild(taskElement);
        });
        
        // Update clear completed button state
        const hasCompleted = this.tasks.some(task => task.completed);
        this.elements.clearCompletedBtn.disabled = !hasCompleted;
    }
    
    /**
     * Create a task DOM element
     */
    createTaskElement(task) {
        const li = document.createElement('li');
        li.className = `task-item ${task.completed ? 'completed' : ''}`;
        li.setAttribute('role', 'listitem');
        li.setAttribute('data-task-id', task.id);
        
        li.innerHTML = `
            <div class="task-checkbox ${task.completed ? 'checked' : ''}" 
                 role="checkbox" 
                 aria-checked="${task.completed}"
                 tabindex="0"
                 aria-label="Mark task as ${task.completed ? 'pending' : 'completed'}">
                ${task.completed ? `
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                        <path d="M20 6L9 17L4 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                ` : ''}
            </div>
            <div class="task-content">
                <span class="task-text">${this.escapeHtml(task.text)}</span>
            </div>
            <div class="task-actions">
                <button class="task-button delete-button" 
                        type="button"
                        aria-label="Delete task: ${this.escapeHtml(task.text)}"
                        title="Delete task">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                        <path d="M3 6H5H21M8 6V4C8 3.46957 8.21071 2.96086 8.58579 2.58579C8.96086 2.21071 9.46957 2 10 2H14C14.5304 2 15.0391 2.21071 15.4142 2.58579C15.7893 2.96086 16 3.46957 16 4V6M19 6V20C19 20.5304 18.7893 21.0391 18.4142 21.4142C18.0391 21.7893 17.5304 22 17 22H7C6.46957 22 5.96086 21.7893 5.58579 21.4142C5.21071 21.0391 5 20.5304 5 20V6H19Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </div>
        `;
        
        // Add event listeners
        const checkbox = li.querySelector('.task-checkbox');
        const deleteBtn = li.querySelector('.delete-button');
        
        checkbox.addEventListener('click', () => this.toggleTask(task.id));
        checkbox.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.toggleTask(task.id);
            }
        });
        
        deleteBtn.addEventListener('click', () => this.deleteTask(task.id));
        
        return li;
    }
    
    /**
     * Update statistics
     */
    updateStats() {
        const total = this.tasks.length;
        const completed = this.tasks.filter(task => task.completed).length;
        const pending = total - completed;
        
        this.elements.totalTasks.textContent = total;
        this.elements.completedTasks.textContent = completed;
        this.elements.pendingTasks.textContent = pending;
    }
    
    /**
     * Show error message
     */
    showError(message) {
        this.elements.taskInputError.textContent = message;
        this.elements.taskInput.setAttribute('aria-invalid', 'true');
        this.elements.taskInput.classList.add('error');
    }
    
    /**
     * Clear error message
     */
    clearError() {
        this.elements.taskInputError.textContent = '';
        this.elements.taskInput.removeAttribute('aria-invalid');
        this.elements.taskInput.classList.remove('error');
    }
    
    /**
     * Show shortcuts modal
     */
    showModal() {
        this.elements.shortcutsModal.classList.add('active');
        this.elements.shortcutsModal.setAttribute('aria-hidden', 'false');
        
        // Focus the close button
        this.elements.modalClose.focus();
        
        // Trap focus within modal
        this.trapFocus(this.elements.shortcutsModal);
    }
    
    /**
     * Hide shortcuts modal
     */
    hideModal() {
        this.elements.shortcutsModal.classList.remove('active');
        this.elements.shortcutsModal.setAttribute('aria-hidden', 'true');
        
        // Return focus to trigger element
        this.elements.shortcutsHelp.focus();
    }
    
    /**
     * Trap focus within an element
     */
    trapFocus(element) {
        const focusableElements = element.querySelectorAll(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        
        if (focusableElements.length === 0) return;
        
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];
        
        const handleTabKey = (e) => {
            if (e.key !== 'Tab') return;
            
            if (e.shiftKey) {
                if (document.activeElement === firstElement) {
                    e.preventDefault();
                    lastElement.focus();
                }
            } else {
                if (document.activeElement === lastElement) {
                    e.preventDefault();
                    firstElement.focus();
                }
            }
        };
        
        element.addEventListener('keydown', handleTabKey);
        
        // Remove listener when modal is closed
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.attributeName === 'class' && 
                    !element.classList.contains('active')) {
                    element.removeEventListener('keydown', handleTabKey);
                    observer.disconnect();
                }
            });
        });
        
        observer.observe(element, { attributes: true });
    }
    
    /**
     * Announce message to screen readers
     */
    announceToScreenReader(message) {
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'polite');
        announcement.setAttribute('aria-atomic', 'true');
        announcement.className = 'visually-hidden';
        announcement.textContent = message;
        
        document.body.appendChild(announcement);
        
        // Remove after announcement
        setTimeout(() => {
            document.body.removeChild(announcement);
        }, 1000);
    }
    
    /**
     * Escape HTML to prevent XSS
     */
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    /**
     * Save tasks to localStorage
     */
    saveTasks() {
        try {
            localStorage.setItem('taskManager_tasks', JSON.stringify(this.tasks));
            localStorage.setItem('taskManager_counter', this.taskIdCounter.toString());
        } catch (error) {
            console.error('Failed to save tasks to localStorage:', error);
            this.announceToScreenReader('Failed to save tasks. Changes may be lost.');
        }
    }
    
    /**
     * Load tasks from localStorage
     */
    loadTasks() {
        try {
            const savedTasks = localStorage.getItem('taskManager_tasks');
            const savedCounter = localStorage.getItem('taskManager_counter');
            
            if (savedTasks) {
                this.tasks = JSON.parse(savedTasks);
            }
            
            if (savedCounter) {
                this.taskIdCounter = parseInt(savedCounter, 10);
                
                // Ensure counter is higher than any existing task ID
                const maxId = this.tasks.reduce((max, task) => Math.max(max, task.id), 0);
                this.taskIdCounter = Math.max(this.taskIdCounter, maxId + 1);
            }
        } catch (error) {
            console.error('Failed to load tasks from localStorage:', error);
            this.tasks = [];
            this.taskIdCounter = 1;
        }
    }
    
    /**
     * Export tasks as JSON
     */
    exportTasks() {
        const dataStr = JSON.stringify(this.tasks, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        
        const link = document.createElement('a');
        link.href = URL.createObjectURL(dataBlob);
        link.download = `tasks-${new Date().toISOString().split('T')[0]}.json`;
        link.click();
        
        this.announceToScreenReader('Tasks exported successfully');
    }
    
    /**
     * Import tasks from JSON file
     */
    importTasks(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const importedTasks = JSON.parse(e.target.result);
                
                if (Array.isArray(importedTasks)) {
                    // Validate and merge tasks
                    const validTasks = importedTasks.filter(task => 
                        task && typeof task.text === 'string' && typeof task.completed === 'boolean'
                    );
                    
                    // Assign new IDs to avoid conflicts
                    validTasks.forEach(task => {
                        task.id = this.taskIdCounter++;
                    });
                    
                    this.tasks = [...this.tasks, ...validTasks];
                    this.saveTasks();
                    this.render();
                    this.updateStats();
                    
                    this.announceToScreenReader(`${validTasks.length} tasks imported successfully`);
                } else {
                    throw new Error('Invalid file format');
                }
            } catch (error) {
                console.error('Failed to import tasks:', error);
                this.announceToScreenReader('Failed to import tasks. Please check the file format.');
            }
        };
        
        reader.readAsText(file);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.taskManager = new TaskManager();
});

// Service Worker registration for offline support (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('ServiceWorker registered: ', registration);
            })
            .catch(registrationError => {
                console.log('ServiceWorker registration failed: ', registrationError);
            });
    });
}