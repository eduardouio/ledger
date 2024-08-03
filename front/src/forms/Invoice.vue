<script setup>
</script>
<template>
    <div>
        <div class="container mx-auto p-4 border rounded-md">
            <div class="flex justify-end items-center gap-3">
                <label for="">Invoice Nro.</label>
                <input type="text" class="input bg-yellow-100 text-end text-red-600 text-2xl"
                    name="number" value="990">
            </div>
            <div class="grid grid-cols-1 gap-2 lg:grid-cols-3">
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Type</span>
                    </label>
                    <select class="select select-bordered w-full" name="type">
                        <option value="invoice" selected>Invoice</option>
                        <option value="bill">Bill</option>
                    </select>
                </div>
                <input type="hidden" class="input w-full">
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Customer</span>
                    </label>
                    <select class="select select-bordered w-full" name="customer">
                        <option>Seleccione...</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Supplier</span>
                    </label>
                    <select class="select select-bordered w-full" name="supplier">
                        <option>Seleccione...</option>
                    </select>
                </div>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-4 gap-3">
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
                        <span class="label-text">Amount</span>
                    </label>
                    <input type="number" step="0.01" class="input w-full" name="amount">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Paid</span>
                    </label>
                    <input type="checkbox" class="checkbox checkbox-success" name="paid">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Notes</span>
                    </label>
                    <textarea class="textarea textarea-bordered w-full" name="notes"></textarea>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Tax</span>
                    </label>
                    <input type="number" step="0.01" class="input w-full" name="tax">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">User</span>
                    </label>
                   <input type="text" class="input w-full">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Status</span>
                    </label>
                    <select class="select w-full" name="status">
                        <option value="draft">Draft</option>
                        <option value="sent">Sent</option>
                        <option value="paid">Paid</option>
                        <option value="cancelled">Cancelled</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="container mx-auto p-2 ">
            <div class="overflow-x-auto">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Invoice</th>
                            <th>Product</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Price</th>
                            <th>Discount</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Invoice</td>
                            <td>Product</td>
                            <td>Description</td>
                            <td>Quantity</td>
                            <td>Price</td>
                            <td>Discount</td>
                            <td>Amount</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="container mx-auto p-2 grid grid-cols-4">
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Invoice</span>
                </label>
                <select class="select select-bordered" name="invoice">
                    <!-- Opciones de facturas -->
                </select>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Product</span>
                </label>
                <select class="select select-bordered" name="product">
                    <!-- Opciones de productos -->
                </select>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Description</span>
                </label>
                <input type="text" class="input" name="description">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Quantity</span>
                </label>
                <input type="number" class="input" name="quantity">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Price</span>
                </label>
                <input type="number" step="0.01" class="input" name="price">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Discount</span>
                </label>
                <input type="number" step="0.01" class="input" name="discount">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Amount</span>
                </label>
                <input type="number" step="0.01" class="input" name="amount">
            </div>
        </div>

    </div>
</template>