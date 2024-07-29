<script setup>
</script>
<template>
    <div>
        <div class="container mx-auto p-4">
            <form class="form-control space-y-4">
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Company</span>
                    </label>
                    <select class="select select-bordered" name="company">
                        <!-- Opciones de compañías -->
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Customer</span>
                    </label>
                    <select class="select select-bordered" name="customer">
                        <!-- Opciones de clientes -->
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Supplier</span>
                    </label>
                    <select class="select select-bordered" name="supplier">
                        <!-- Opciones de proveedores -->
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Type</span>
                    </label>
                    <select class="select select-bordered" name="type">
                        <option value="invoice">Invoice</option>
                        <option value="bill">Bill</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Date</span>
                    </label>
                    <input type="date" class="input input-bordered" name="date">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Due Date</span>
                    </label>
                    <input type="date" class="input input-bordered" name="due_date">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Number</span>
                    </label>
                    <input type="text" class="input input-bordered" name="number">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Amount</span>
                    </label>
                    <input type="number" step="0.01" class="input input-bordered" name="amount">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Paid</span>
                    </label>
                    <input type="checkbox" class="checkbox" name="paid">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Notes</span>
                    </label>
                    <textarea class="textarea textarea-bordered" name="notes"></textarea>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Tax</span>
                    </label>
                    <input type="number" step="0.01" class="input input-bordered" name="tax">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">User</span>
                    </label>
                    <select class="select select-bordered" name="user">
                        <!-- Opciones de usuarios -->
                    </select>
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Status</span>
                    </label>
                    <select class="select select-bordered" name="status">
                        <option value="draft">Draft</option>
                        <option value="sent">Sent</option>
                        <option value="paid">Paid</option>
                        <option value="cancelled">Cancelled</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        <div class="container mx-auto p-4">
            <form class="form-control space-y-4">
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
                    <input type="text" class="input input-bordered" name="description">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Quantity</span>
                    </label>
                    <input type="number" class="input input-bordered" name="quantity">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Price</span>
                    </label>
                    <input type="number" step="0.01" class="input input-bordered" name="price">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Discount</span>
                    </label>
                    <input type="number" step="0.01" class="input input-bordered" name="discount">
                </div>
                <div class="form-group">
                    <label class="label">
                        <span class="label-text">Amount</span>
                    </label>
                    <input type="number" step="0.01" class="input input-bordered" name="amount">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>

    </div>
</template>