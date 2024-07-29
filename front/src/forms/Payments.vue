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
        <span class="label-text">Invoice</span>
      </label>
      <select class="select select-bordered" name="invoice">
        <!-- Opciones de facturas -->
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
        <span class="label-text">Amount</span>
      </label>
      <input type="number" step="0.01" class="input input-bordered" name="amount">
    </div>
    <div class="form-group">
      <label class="label">
        <span class="label-text">Notes</span>
      </label>
      <textarea class="textarea textarea-bordered" name="notes"></textarea>
    </div>
    <div class="form-group">
      <label class="label">
        <span class="label-text">Method</span>
      </label>
      <select class="select select-bordered" name="method">
        <option value="cash">Cash</option>
        <option value="credit_card">Credit Card</option>
        <option value="debit_card">Debit Card</option>
        <option value="check">Check</option>
        <option value="bank_transfer">Bank Transfer</option>
        <option value="other">Other</option>
      </select>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>
</template>