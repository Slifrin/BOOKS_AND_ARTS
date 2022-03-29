#include <iostream>
#include <string>

class Component {
public:
    virtual ~Component() {}
    virtual std::string Operation() const = 0;
};


class ConcreteComponent: public Component {
public:
    std::string Operation() const override {
        return "ConcreteComponent";
    }
};

class Decorator : public Component {
protected:
    Component* wrapped_component;
public:
    Decorator(Component* component) : wrapped_component(component){}
    std::string Operation() const override {
        return this->wrapped_component->Operation();
    }
};

class ConcreteDecoratorA : public Decorator {
public:
    ConcreteDecoratorA(Component* component) : Decorator(component){}
    std::string Operation() const override {
        return "ConcreteDecoratorA(" + Decorator::Operation() + ")";
    }
};
class ConcreteDecoratorB : public Decorator {
public:
    ConcreteDecoratorB(Component* component) : Decorator(component){}
    std::string Operation() const override {
        return "ConcreteDecoratorB(" + Decorator::Operation() + ")";
    }
};

void ClientCode(Component* component){
    std::cout << "RESULT:: " << component->Operation();
    std::cout << "\n\n";
}


int main() {
    Component* simple = new ConcreteComponent;
    std::cout << "Client: I've got a simple component:\n";
    ClientCode(simple);

    Component* decorator1 = new ConcreteDecoratorA(simple);
    Component* decorator2 = new ConcreteDecoratorB(decorator1);
    std::cout << "Client: Now I've got a decorated component:\n";
    ClientCode(decorator1);
    ClientCode(decorator2);

    delete simple;
    delete decorator1;
    delete decorator2;
    return 0;
}

