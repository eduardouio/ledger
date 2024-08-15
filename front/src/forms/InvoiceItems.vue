<script setup>
console.log('InvoiceItems.vue');
</script>
<template>
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
</template>