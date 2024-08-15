<script setup>
import { IconBuildingBank } from '@tabler/icons-vue';
</script>
<template>
    <div class="border p-4 rounded-md">
        <div class="container mx-auto p-2">
            <div class="flex justify-between items-center gap-3">
                <span class="badge bg-red-500 text-lg p-3 text-white">Draft</span>
                <span class="flex gap-3">
                    <label for="">Invoice Nro.</label>
                    <input type="text" class="input bg-yellow-100 text-end text-red-600 text-2xl" name="number" value="990">
                </span>
            </div>
            <div class="grid grid-cols-1 gap-2 lg:grid-cols-3 md:grid-cols-2">
                <div class="form-group w-full">
                    <label class="label">
                        <span class="label-text">Type</span>
                    </label>
                    <select class="select select-bordered w-full" name="type">
                        <option value="invoice" selected>Invoice</option>
                        <option value="bill">Bill</option>
                    </select>
                </div>
                <div class="form-group w-full">
                    <label class="label">
                        <span class="label-text">Customer</span>
                    </label>
                    <select class="select select-bordered w-full" name="customer">
                        <option>Seleccione...</option>
                    </select>
                </div>
                <div class="form-group w-full">
                    <label class="label">
                        <span class="label-text">Supplier</span>
                    </label>
                    <select class="select select-bordered w-full" name="supplier">
                        <option>Seleccione...</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Date</span>
                    </label>
                    <input type="date" class="input w-full" name="date">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Due Date</span>
                    </label>
                    <input type="date" class="input w-full" name="due_date">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Status</span>
                    </label>
                    <select class="select w-full" name="status">
                        <option value="draft">Draft</option>
                        <option value="sent">Sent</option>
                        <option value="cancelled">Cancelled</option>
                    </select>
                </div>
            </div>
        </div>
        <d  iv class="container mx-auto p-2 ">
            <div class="p-1">
                <button class="btn btn-sm">Add Item</button>
            </div>
            <div class="overflow-x-auto">
                <table class="table table-zebra table-fixed table-sm">
                    <thead>
                        <tr class="bg-blue-50 text-cyan-500 text-center">
                            <th class="w-1/12">#</th>
                            <th class="w-7/12">Description</th>
                            <th class="w-1/12">Quantity</th>
                            <th class="w-1/12">Price</th>
                            <th class="w-1/12">Discount</th>
                            <th class="w-1/12">Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="text-sm">
                            <td class="text-center">1</td>
                            <td>Este es mi producto o servicio</td>
                            <td class="text-end">2</td>
                            <td class="text-end">12,02</td>
                            <td class="text-end">0,00</td>
                            <td class="text-end">24.04</td>
                        </tr>
                        <tr class="text-sm">
                            <td class="text-center">2</td>
                            <td>Este es mi producto o servicio</td>
                            <td class="text-end">2</td>
                            <td class="text-end">12,02</td>
                            <td class="text-end">0,00</td>
                            <td class="text-end">24.04</td>
                        </tr>
                        <tr class="text-sm">
                            <td class="text-center">3</td>
                            <td>Este es mi producto o servicio</td>
                            <td class="text-end">2</td>
                            <td class="text-end">12,02</td>
                            <td class="text-end">0,00</td>
                            <td class="text-end">24.04</td>
                        </tr>
                        <tr class="text-xl font-bold">
                            <td class="text-end text-success" colspan="5">SUMS</td>
                            <td class="text-end">24.04</td>
                        </tr>
                        <tr class="text-xl font-bold">
                            <td class="text-end text-success" colspan="5">TAXES</td>
                            <td class="text-end">4.04</td>
                        </tr>
                        <tr class="text-xl font-bold">
                            <td class="text-end bg-green-500" colspan="5">TOTAL</td>
                            <td class="text-end bg-green-500">28.08</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </d>
        <div class="container mx-auto p-2">
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Notes</span>
                    </label>
                    <textarea class="textarea textarea-bordered w-full" name="notes"></textarea>
                </div>
        </div>
        <div class="container mx-auto p-2">
            <div class="flex flex-col gap-3 lg:flex-row lg:justify-end lg:space-x-3">
    <button class="btn btn-sm btn-error">Cancel</button>
    <button class="btn btn-sm btn-success">
        <IconBuildingBank class="w-5 h-5" stroke-width="1"/>
        Mark Paid
    </button>
    <button class="btn btn-sm">Save</button>
</div>

</div>
    </div>
</template>