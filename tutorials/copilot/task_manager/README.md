# Task Manager Web Application

A modern, accessible, and responsive task management web application built with vanilla HTML, CSS, and JavaScript.

## Features

### Core Functionality
- ✅ **Add Tasks** - Create new tasks with validation and duplicate detection
- ✅ **Mark Complete** - Toggle task completion status with visual feedback
- ✅ **Delete Tasks** - Remove individual tasks or clear all completed tasks
- ✅ **Filter Tasks** - View all, pending, or completed tasks
- ✅ **Task Statistics** - Real-time counters for total, completed, and pending tasks

### User Experience
- 🎨 **Modern Design** - Clean, professional interface with smooth animations
- 📱 **Responsive Layout** - Works perfectly on desktop, tablet, and mobile devices
- 🌙 **Dark Mode Support** - Automatically adapts to system preferences
- ⚡ **Fast Performance** - Optimized for speed with efficient DOM updates
- 💾 **Local Storage** - Tasks persist between browser sessions
- 🔄 **Cross-tab Sync** - Changes sync across multiple browser tabs

### Accessibility
- ♿ **WCAG 2.1 AA Compliant** - Full accessibility support
- ⌨️ **Keyboard Navigation** - Complete keyboard accessibility
- 🔊 **Screen Reader Support** - Comprehensive ARIA labels and announcements
- 🎯 **Focus Management** - Clear focus indicators and logical tab order
- 📢 **Live Regions** - Dynamic content updates announced to assistive technologies

### Advanced Features
- ⌨️ **Keyboard Shortcuts** - Quick actions for power users
- 🎭 **Empty States** - Helpful guidance when no tasks exist
- ⚠️ **Error Handling** - Graceful error handling with user feedback
- 🔒 **XSS Protection** - Safe HTML rendering with input sanitization
- 📤 **Export/Import** - Backup and restore tasks (extensible feature)

## File Structure

```
task_manager/
├── index.html          # Main HTML structure
├── css/
│   └── styles.css      # Complete styling and responsive design
├── js/
│   └── app.js          # Application logic and functionality
└── README.md           # This documentation
```

## Browser Support

- ✅ Chrome 88+
- ✅ Firefox 85+
- ✅ Safari 14+
- ✅ Edge 88+

## Getting Started

1. **Clone or download** the files to your local machine
2. **Open** `index.html` in a modern web browser
3. **Start adding tasks** and organizing your day!

No build process or dependencies required - just open and use!

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Add new task (when input is focused) |
| `Space` | Toggle task completion (when task is focused) |
| `Delete` | Delete task (when task is focused) |
| `Esc` | Close modal or clear input |
| `A` | Focus task input |
| `1` | Show all tasks |
| `2` | Show pending tasks |
| `3` | Show completed tasks |
| `C` | Clear completed tasks |
| `?` | Show keyboard shortcuts help |

## Technical Details

### Architecture
- **Vanilla JavaScript** - No frameworks or libraries required
- **Class-based Structure** - Clean, maintainable code organization  
- **Event-driven Design** - Efficient event handling and delegation
- **Local Storage API** - Persistent data storage

### CSS Features
- **CSS Custom Properties** - Consistent theming and easy customization
- **CSS Grid & Flexbox** - Modern layout techniques
- **CSS Animations** - Smooth transitions and micro-interactions
- **Media Queries** - Responsive design breakpoints
- **Print Styles** - Optimized for printing task lists

### JavaScript Features
- **ES6+ Syntax** - Modern JavaScript features
- **Local Storage** - Data persistence
- **Event Delegation** - Efficient event handling
- **ARIA Support** - Dynamic accessibility attributes
- **Input Validation** - Client-side form validation
- **Error Handling** - Graceful error recovery

### Accessibility Features
- **Semantic HTML** - Proper HTML5 semantic elements
- **ARIA Labels** - Comprehensive accessibility labels
- **Focus Management** - Logical focus flow and trap
- **Screen Reader Support** - Live announcements and descriptions
- **High Contrast** - Sufficient color contrast ratios
- **Reduced Motion** - Respects user motion preferences

## Customization

### Colors
Modify CSS custom properties in `:root` to change the color scheme:

```css
:root {
    --primary-color: #6366f1;    /* Main accent color */
    --secondary-color: #10b981;  /* Success/completed color */
    --danger-color: #ef4444;     /* Delete/error color */
}
```

### Typography
Change the font family by updating:

```css
:root {
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
```

### Layout
Adjust spacing using the spacing scale:

```css
:root {
    --space-4: 1rem;    /* Base spacing unit */
    --space-8: 2rem;    /* Section spacing */
}
```

## Performance Considerations

- **Efficient DOM Updates** - Minimal DOM manipulation
- **Event Delegation** - Single event listeners for dynamic content
- **Local Storage Optimization** - Batched storage operations
- **CSS Optimization** - Minimal reflows and repaints
- **Image Optimization** - SVG icons for crisp display at any size

## Security Features

- **XSS Prevention** - HTML escaping for user input
- **Input Validation** - Client-side validation with length limits
- **Safe DOM Manipulation** - Sanitized content insertion

## Future Enhancements

The application architecture supports easy extension with:

- 🗓️ **Due Dates** - Add date pickers and sorting
- 🏷️ **Categories/Tags** - Organize tasks by type
- 🔍 **Search** - Find tasks quickly
- ☁️ **Cloud Sync** - Backup to cloud services
- 👥 **Collaboration** - Share task lists
- 📊 **Analytics** - Task completion insights
- 🔔 **Notifications** - Reminder system
- 📱 **PWA Support** - Install as mobile app

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

Built with ❤️ for productivity and accessibility.