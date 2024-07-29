<script setup></script>
<template>
    <div class="container mx-auto p-4">
        <form class="form-control space-y-4">
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Tax ID</span>
                </label>
                <input type="text" class="input input-bordered" name="tax_id">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Name</span>
                </label>
                <input type="text" class="input input-bordered" name="name">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Address</span>
                </label>
                <input type="text" class="input input-bordered" name="address">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Phone</span>
                </label>
                <input type="text" class="input input-bordered" name="phone">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Email</span>
                </label>
                <input type="email" class="input input-bordered" name="email">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Website</span>
                </label>
                <input type="url" class="input input-bordered" name="website">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Logo</span>
                </label>
                <input type="file" class="file-input file-input-bordered" name="logo">
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Notes</span>
                </label>
                <textarea class="textarea textarea-bordered" name="notes"></textarea>
            </div>
            <div class="form-group">
                <label class="label">
                    <span class="label-text">Manager</span>
                </label>
                <select class="select select-bordered" name="manager">
                    <!-- Opciones de usuarios -->
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>

</template>
