const getData = () => ({
  items: [
    { 'id': 1, 'servico': 'Alinhamento' },
    { 'id': 2, 'servico': 'Balanceamento' },
    { 'id': 3, 'servico': 'Troca de Óle' },
  ],
  cliente: {},
  searchCliente: '',

  init() {
    // watch - monitora ações
    this.$watch('searchCliente', (newValue, oldValue) => {
      if (newValue.length >= 3) {
        this.getCliente(newValue)
      }
    })
  },



  addItem() {
    this.items.push({ 'id': 4, 'servico': 'Higienização' })
  },

  getCliente(newValue) {
    const search = newValue
    fetch(`/api/v1/crm/cliente/?search=${search}`)
      .then(response => response.json())
      .then(data => {
        this.cliente.id = data[0].id
        this.cliente.endereco = data[0].endereco
        this.cliente.bairro = data[0].bairro
      })
  },
})
