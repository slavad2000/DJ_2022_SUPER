class Menu_select {
    constructor(selector, options) {
        this.$el = selector;
        this.$options = options;
        this.#render();
        this.$buttom = this.$el.querySelector('.items_name');
        this.#setup();
    }
    #render() {
    }
    #setup() {
        this.clickButtom = this.clickButtom.bind(this);
        this.$el.addEventListener('click', this.clickButtom)
    }

    open() {
        this.$el.classList.add('open');
    }

    close() {
        this.$el.classList.remove('open');
    }

    get isOpen() {
        return this.$el.classList.contains('open');
    }    

    toggle() {
        this.isOpen ? this.close():this.open(); 
    }

    clickButtom(event) {
        if (event.target.classList.contains('items_name'))
            this.toggle();
        else
            this.$options.onSelect  ? this.$options.onSelect(event.target.id):null
    }
}
