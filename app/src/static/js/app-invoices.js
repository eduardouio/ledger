
const app = Vue.createApp({
  // Datos reactivos
  data() {
    return {
      message: '',
      confirm_delete:false,
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
      company: companyData.map((itm) => {
        return {
          id: itm.pk,
          ...itm.fields
        }
      })[0],
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
        discount: 0,
        delete: false
      }
    };
  },
  // Métodos de la app
  methods: {
    addNewItem() {
      if (this.new_item.product == null || this.new_item.quantity == 0){
        this.message = 'Product/Service es required and Quantity must be greater than 0';
        return;
      }
      if (this.new_item.discount == '' || this.new_item.discount == null){ 
        this.new_item.discount = 0;
      }
      this.invoice_items.push({...this.new_item});
      this.new_item = {
        product: null,
        quantity: 0,
        price: 0,
        discount: 0
      };
      this.is_disabled_add_item = true
      this.$refs.quantityInput.focus();
      this.message = ''
    },
    selectItem(){
      this.new_item.price = this.new_item.product.price;
      this.new_item.id = this.new_item.product.id;
      this.new_item.quantity = 1;
      this.is_disabled_add_item = false;
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
    setDueDate(){
      let start_date = new Date(this.invoice_headers.date);
      let days = this.invoice_headers.pay_terms;
      start_date.setDate(start_date.getDate() + days);
      let due_year = start_date.getFullYear();
      let due_month = String(start_date.getMonth() + 1).padStart(2, '0');
      let due_day = String(start_date.getDate()).padStart(2, '0');
      this.invoice_headers.due_date = `${due_year}-${due_month}-${due_day}`;
    },
    deleteItem(index){
      this.invoice_items.splice(index, 1);
    },
    saveInvoice(){
      
    }
  },
  // Ciclo de vida de la app
  mounted() {
    console.log('App mounted!');
  },
  // Propiedades computadas
  computed: {
    new_item_total() {
      return (
        this.new_item.quantity * this.new_item.price) 
        - this.new_item.discount;
    },
    subtotal_1() {
      let subtotal_1 = this.invoice_items.reduce((acc, item) => {
        return acc + (item.quantity * item.price);
      },0);
      subtotal_1 = parseFloat(subtotal_1);
      return subtotal_1.toFixed(2);
    },
    discount() {
      let discount = this.invoice_items.reduce((acc, item) => {
        return acc + (item.discount * 1 );
      }, 0);
      discount = parseFloat(discount);
      return discount.toFixed(2);

    },
    subtotal_2() {
      let subtotal_2 = this.subtotal_1 - this.discount;
      return subtotal_2.toFixed(2);
    },
    tax() {
      let tax = this.subtotal_2 * this.company.tax_in_sales / 100;
      return tax.toFixed(2);
    },
    total() {
      let total = parseFloat(this.subtotal_2 + this.tax);
      return total.toFixed(2);
    },
    isCompleteInvoice() {
      return this.invoice_headers.customer 
            && this.invoice_headers.date 
            && this.invoice_headers.due_date
            && this.invoice_items.length > 0;
    },
}});

app.config.compilerOptions.delimiters = ['[[', ']]'];
const vm = app.mount('#app');