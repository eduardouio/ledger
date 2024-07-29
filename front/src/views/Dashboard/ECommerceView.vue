<script setup lang="js">
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import 
  { 
    IconHomeDollar, IconClipboardData, IconUsers, IconPlus, IconList, 
    IconUserDollar, IconTruck, IconBuildingFactory2, IconBuildings, 
    IconBriefcase
  } 
from '@tabler/icons-vue';
</script>

<template>
  <DefaultLayout>
    <div class="grid grid-cols-3 gap-4 md:grid-cols-2 md:gap-6 xl:grid-cols-4 p-4 border rounded-md border-cyan-300">
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
        <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl border border-cyan-500">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl left-4 -top-6 border bg-gray-100 border-cyan-500">
               <IconUserDollar class="h-8 w-8 text-cyan-500"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">Bills</p>
                <div class="flex space-x-2 text-sm">
                    <IconClipboardData class="h-5 w-5 text-green-600"/>
                     <p class="text-gray-600">Report</p> 
                </div>
                <div class="flex space-x-2 text-gray-400 text-sm my-3">
                    <IconUsers class="h-5 w-5 text-green-600"/>
                     <p class="text-gray-600">Suppliers</p> 
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
        <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl border border-cyan-500">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl left-4 -top-6 border bg-gray-100 border-cyan-500">
               <IconTruck class="h-8 w-8 text-cyan-500"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">Transport</p>
                <div class="flex space-x-2 text-sm">
                    <IconClipboardData class="h-5 w-5 text-green-600"/>
                     <p class="text-gray-600">Report</p> 
                </div>
                <div class="flex space-x-2 text-gray-400 text-sm my-3 ">
                    <IconUsers class="h-5 w-5 text-green-600"/>
                     <p class="text-gray-600">Suppliers</p> 
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
        <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl border border-cyan-500">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl left-4 -top-6 border bg-gray-100 border-cyan-500">
               <IconBuildingFactory2 class="h-8 w-8 text-cyan-500"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">PEquipment</p>
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
        <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl border border-cyan-500">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl left-4 -top-6 border bg-gray-100 border-cyan-500">
               <IconBuildings class="h-8 w-8 text-cyan-500"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">Rents</p>
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
        <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl border border-cyan-500">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl left-4 -top-6 border bg-gray-100 border-cyan-500">
               <IconBriefcase class="h-8 w-8 text-cyan-500"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">Labor</p>
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
    </div>
  </DefaultLayout>
</template>
