<script setup>
</script>
<template>
    <div class="container mx-auto p-4">
        <form class="form-control space-y-4">
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Code</span>
                </label>
                <input type="text" class="input input-bordered" name="code">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Name</span>
                </label>
                <input type="text" class="input input-bordered" name="name">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Type</span>
                </label>
                <select class="select select-bordered" name="type">
                    <option value="asset">Activo</option>
                    <option value="liability">Pasivo</option>
                    <option value="equity">Patrimonio</option>
                    <option value="income">Ingreso</option>
                    <option value="expense">Gasto</option>
                </select>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Description</span>
                </label>
                <textarea class="textarea textarea-bordered" name="description"></textarea>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Parent Account</span>
                </label>
                <select class="select select-bordered" name="parent_account">
                    <!-- Opciones de cuentas parent -->
                </select>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Company</span>
                </label>
                <select class="select select-bordered" name="company">
                    <!-- Opciones de compañías -->
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

</template>
