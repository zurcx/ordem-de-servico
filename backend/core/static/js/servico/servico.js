const getData = () => ({
  items: [
    { 'id': 1, 'servico': 'Alinhamento' },
    { 'id': 2, 'servico': 'Balanceamento' },
    { 'id': 3, 'servico': 'Troca de Óle' },
  ],
  clientes: [],
  cliente: {},
  clienteSelecionado: {},
  searchCliente: '',
  servico: [],
  servico: {},
  servicoSelecionado: {},
  servicoCliente: '',
  ordemServico: {},

  init() {
    // watch - monitora ações
    this.$watch('searchCliente', (newValue, oldValue) => {
      if (newValue.length >= 3) {
        this.getClientes(newValue)
      }
    })
    this.$watch('searchServico', (newValue, oldValue) => {
      if (newValue.length >= 3) {
        this.getServicos(newValue)
      }
    })
  },



  addItem() {
    this.items.push({ 'id': 4, 'servico': 'Higienização' })
  },

  getClientes(newValue) {
    const search = newValue
    fetch(`/api/v1/crm/cliente/?search=${search}`)
      .then(response => response.json())
      .then(data => {
        this.clientes = data
      })
  },

  getCliente(cliente) {
    this.clienteSelecionado = cliente
  },

  getServicos(newValue) {
    const search = newValue
    fetch(`/api/v1/servico/servico/?search=${search}`)
      .then(response => response.json())
      .then(data => {
        this.servicos = data
      })
  },

  getservico(servico) {
    this.servicoSelecionado = servico
  },

})
