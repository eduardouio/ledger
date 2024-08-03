<script setup lang="ts">
import { ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import Invoice from '@/forms/Invoice.vue';

const pageTitle = ref('New Invoice')

</script>
<template>
    <DefaultLayout>
        <BreadcrumbDefault  :pageTitle="pageTitle"/>
        <Invoice/>
    </DefaultLayout>
</template>