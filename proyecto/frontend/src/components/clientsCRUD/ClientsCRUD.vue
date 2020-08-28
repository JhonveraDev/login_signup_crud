<template>
    <div class="clients-container">
        <div v-for="client of clients" class="card mt-4" >
            <div class="card-body">
                <div><span class="font-weight-bold">Nombre:</span> {{ client.name }}</div>
                <div><span class="font-weight-bold">Edad:</span> {{ client.age }}</div>
                <div><span class="font-weight-bold">Dirección:</span> {{ client.address }}</div>
                <div><span class="font-weight-bold">Teléfono:</span> {{ client.phone }}</div>
                <div><span class="font-weight-bold">Email:</span> {{ client.email }}</div>
                <div class="d-flex justify-content-end">
                    <button class="btn btn-info" data-toggle="modal" data-target="#clientsModal" v-on:click="handleClickUpdateClient" v-bind:data-id="client.id">Editar</button>
                    <button class="btn btn-danger ml-3" v-on:click="handleClickDeleteClient" v-bind:data-id="client.id">Eliminar</button>
                </div>
            </div>
        </div>
        <button class="btn btn-success mt-4" data-toggle="modal" data-target="#clientsModal">Añadir cliente</button>

        <!-- Modal -->
        <div id="clientsModal" class="modal fade" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Crear o editar cliente nuevo</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form>
                        <input id="clientId" type="hidden" :value="currentClient.id" /> 
                        <div class="form-group">
                            <label for="name">Nombre: </label>
                            <input id="name" type="text" v-model="currentClient.name" />
                        </div>
                        <div class="form-group">
                            <label for="age">Edad: </label>
                            <input id="age" type="number" v-model="currentClient.age" />
                        </div>
                        <div class="form-group">
                            <label for="address" >Dirección: </label>
                            <input id="address" type="text" v-model="currentClient.address"/>
                        </div>
                        <div class="form-group">
                            <label for="phone">Teléfono: </label>
                            <input id="phone" type="text" v-model="currentClient.phone" />
                        </div>
                        <div class="form-group">
                            <label for="email">Email: </label>
                            <input id="email" type="email" v-model="currentClient.email" />
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                    <button type="button" class="btn btn-success" v-on:click="handleClickSaveClient">Guardar cliente</button>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    async function getClients(){
        let clients = await axios.get('/api/clients/get');
        
        return clients.data.clients;
    }

    async function saveClient(currentClient, clients){
        let newClient = {
            id: currentClient.id,
            name: currentClient.name,
            age: currentClient.age,
            address: currentClient.address,
            phone: currentClient.phone,
            email: currentClient.email
        };
        let saveResult = await axios.post('/api/clients/createOrUpdate/', newClient);
        
        if(saveResult.data.id) {
            newClient['id'] = saveResult.data.id;

            clients.push(newClient);
        }
        
        alert("Cliente guardado satisfactoriamente.");
    }

    async function deleteClient(clientId, clients){
        let deleteResult = await axios.get(`/api/clients/delete/${clientId}`);
        
        if(deleteResult.data.deleted){
            for (let i =0; i < clients.length; i++) {
                if (clients[i].id == clientId) {
                    clients.splice(i, 1);
                    break;
                }
            }

            alert("Cliente borrado satisfactoriamente.");
        }
    }

    export default {
        data: () => ({
            clients: [],
            currentClient: {
                id: '',
                name: '',
                age: '',
                address: '',
                phone: '',
                email: ''
            }
        }),
        created: async function () {
            this.clients = await getClients();
        },
        methods: {
            handleClickSaveClient: function(event) {
                saveClient(this.currentClient, this.clients);
            },
            handleClickDeleteClient: function(event) {
                let clientId = event.target.getAttribute('data-id');
                deleteClient(clientId, this.clients);
            },
            handleClickUpdateClient: function(event) {
                let clientId = event.target.getAttribute('data-id');
                let currentClient = {};

                for (let i = 0; i < this.clients.length; i++) {
                    if (this.clients[i].id == clientId) {
                        this.currentClient = this.clients[i];
                        break;
                    }
                }
            }
        }
    };
</script>

<style lang="scss" scoped>
    @import 'clientsCRUD.scss';
</style>