<script setup lang="js">
import { IconHomeDollar, IconClipboardData, IconUsers, IconPlus, IconList } from '@tabler/icons-vue';
import { ref } from 'vue'

const props = defineProps({
  category: {
    type: String,
    required: true
  }
})


</script>
<template>
  <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl border border-cyan-500">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl left-4 -top-6 border bg-gray-100 border-cyan-500">
               <IconHomeDollar class="h-8 w-8 text-cyan-500"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">Sales</p>
                <div class="flex space-x-2 text-sm">
                    <IconClipboardData class="h-5 w-5 text-green-600"/>
                     <p class="text-gray-600">Report</p> 
                </div>
                <div class="flex space-x-2 text-gray-400 text-sm my-3">
                    <IconUsers class="h-5 w-5 text-green-600"/>
                     <p class="text-gray-600">Customers</p> 
                </div>
                <div class="border-t-2 "></div>

                <div class="flex justify-between pt-4">
                    <button class="btn btn-sm ">
                      <IconPlus class="h-5 w-5 text-white"/>
                      New
                    </button>
                    <button class="btn btn-sm">
                      <IconList class="h-5 w-5 text-white"/>
                      List
                    </button>
                </div>
            </div>
        </div>
</template>
