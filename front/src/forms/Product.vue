<script setup>
</script>
<template>
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
                    <span class="label-text">Account</span>
                </label>
                <select class="select select-bordered" name="account">
                    <!-- Opciones de cuentas -->
                </select>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Name</span>
                </label>
                <input type="text" class="input input-bordered" name="name">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Description</span>
                </label>
                <textarea class="textarea textarea-bordered" name="description"></textarea>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Price</span>
                </label>
                <input type="number" step="0.01" class="input input-bordered" name="price">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Tax</span>
                </label>
                <input type="number" step="0.01" class="input input-bordered" name="tax">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Stock</span>
                </label>
                <input type="number" class="input input-bordered" name="stock">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Image</span>
                </label>
                <input type="file" class="file-input file-input-bordered" name="image">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Type</span>
                </label>
                <select class="select select-bordered" name="type">
                    <option value="product">Product</option>
                    <option value="service">Service</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

</template>