<script setup></script>
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
                    <span class="label-text">Description</span>
                </label>
                <textarea class="textarea textarea-bordered" name="description"></textarea>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Amount</span>
                </label>
                <input type="number" step="0.01" class="input input-bordered" name="amount">
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
                    <span class="label-text">Notes</span>
                </label>
                <textarea class="textarea textarea-bordered" name="notes"></textarea>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">User</span>
                </label>
                <select class="select select-bordered" name="user">
                    <!-- Opciones de usuarios -->
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

</template>