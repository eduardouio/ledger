<script setup lang="js">
import { IconCubePlus, IconSearch, IconCirclePlus, IconPlus, IconCancel } from '@tabler/icons-vue'
import { ref } from 'vue'

const modalIsOpen = ref(false)

const filteredProducts = ref([
    { id: 1, name: 'Mouse genius 300dpi Gamer', available: 10 },
    { id: 2, name: 'Keyboard altima-34sc backligth', available: 5 },
    { id: 3, name: 'Producto 3', available: 3 },
    { id: 4, name: 'Producto 4', available: 8 },
    { id: 5, name: 'Producto 5', available: 2 },
  ])

const searchProduct = () => {
    console.log('Buscando producto...')
  }

const addProduct = () => {
    console.log('Agregando producto...')
  }

const closeModal = () => {
    console.log('Cerrando modal...')
}

const openModal = () => {
    const modal = document.getElementById('myModal')
    modal.showModal();
    console.log('Abriendo modal...')
}


</script>
<template>
  <div>
    <!-- Botón para abrir el modal -->
    <button class="btn btn-sm bg-blue-900" @click="openModal">
      <IconCubePlus stroke-width="1.5" class="text-withe h-5 w-5" />
      Add Item
    </button>
    <!-- Modal -->
    <dialog id="myModal" class="modal">
      <div class="bg-white p-10 rounded-xl w-full md:w-3/4 lg:w-2/4 ">
          <div class="flex justify-between gap-3 mb-3">
            <label class="input input-bordered flex justify-between gap-2 input-sm w-full">
              <input type="text" placeholder="Buscar producto...">
                <IconSearch class="h-5 w-5" />
              </label>
          </div>  
            <ul class="bg-base-100 w-full">
              <li v-for="product in filteredProducts" :key="product.id" class="flex justify-between p-2 border-b border-slate-200 hover:bg-yellow-200">
                <div>
                  <span class="badge text-green-600">Stock: {{ product.available }}</span>
                  {{ product.name }}
                </div>
                <button class="btn btn-sm bg-blue-500">
                  <IconCirclePlus class="w-5 h-5" />
                  Select
                </button>
              </li>
            </ul>
          <div class="modal-action">
              <button class="btn btn-primary btn-sm" @click="addProduct">
                <IconPlus class="h-5 w-5" />
                Agregar
              </button>
              <button class="btn btn-error btn-sm" @click="closeModal">
                <IconCancel class="h-5 w-5" />
                Cancelar
              </button>
            </div>
        </div>
    </dialog>
  </div>
</template>
<style scoped>
.modal {
  background-color: rgba(0, 0, 0, 0.5);
}
</style>