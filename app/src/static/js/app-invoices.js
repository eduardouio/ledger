
const app = Vue.createApp({
  // Datos reactivos
  data() {
    return {
      customers: customersData.map((itm) => {
        return {
          id: itm.pk,
          ...itm.fields
        }
      }),
      products: productsData.map((itm) => {
        return {
          id: itm.pk,
          ...itm.fields
        }
      }),
      invoice_headers: {
        customer:null,
        date: null,
        pay_terms: null,
        due_date: null,
        number: invoice_number,
        status: null,
        subtotal_1: 0,
        subtotal_2:0,
        discount:0,
        tax:0,
        total:0
      },
      invoice_items: [],
      new_item: {
        product: null,
        id:null,
        quantity: 0,
        price: 0,
        discount: 0
      }
    };
  },
  // Métodos de la app
  methods: {
    addNewItem() {
      console.log('Estamos llamando a la funcion de addNewItem');
    },
    selectItem(event){
      this.new_item.price = this.new_item.product.price;
      this.new_item.id = this.new_item.product.id;
      this.new_item.quantity = 1;
    },
    setCustomer(){
        let today = new Date();
        let year = today.getFullYear();
        let month = String(today.getMonth() + 1).padStart(2, '0');
        let day = String(today.getDate()).padStart(2, '0');
        this.invoice_headers.date = `${year}-${month}-${day}`;
        let days = this.invoice_headers.customer.pay_terms ?? 0; 
        this.invoice_headers.pay_terms = days;
        if (days == 0){
            console.log('Cliente de contado')
            this.invoice_headers.due_date = `${year}-${month}-${day}`;
            return;
        }
        today.setDate(today.getDate() + days);
        let due_year = today.getFullYear();
        let due_month = String(today.getMonth() + 1).padStart(2, '0');
        let due_day = String(today.getDate()).padStart(2, '0');
        this.invoice_headers.due_date = `${due_year}-${due_month}-${due_day}`;
    },
  },
  // Ciclo de vida de la app
  mounted() {
    console.log('App mounted!');
  },
  // Propiedades computadas
  computed: {
    new_item_total() {
      return (this.new_item.quantity * this.new_item.price) - this.new_item.discount;
    },
    subtotal_1() {
      return this.invoice_items.reduce((acc, item) => {
        return acc + (item.quantity * item.price) - item.discount;
      }, '0.00');
    },
    discount() {
      return this.invoice_items.reduce((acc, item) => {
        return acc + item.discount;
      }, '0.00');
    },
    subtotal_2() {
      return this.subtotal_1 - this.discount;
    },
    tax() {
      return this.subtotal_2 * 0.12;
    },
    total() {
      return this.subtotal_2 + this.tax;
    }
}});

app.config.compilerOptions.delimiters = ['[[', ']]'];
const vm = app.mount('#app');