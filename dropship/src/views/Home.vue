<template>

  <div class="mx-20 my-4">
    <div class="flex flex-row items-center justify-between">
      <h2 class="text-5xl font-black text-gray-900">Users</h2>
      <Button icon-left="plus">New List</Button>
    </div>
    <div>
      <ul>
            <li
              class="flex flex-row space-y-2 items-center justify-between"
              v-for="user in users.data"
              :key="user.first_name"
            >
              
                {{ user.first_name }}
            
              
            </li>
          </ul>
      </div>
  
    </div>
  
  </template>
  
  <script setup>
  import { Dialog, createListResource, Card, Input } from 'frappe-ui'
  import { reactive, ref, computed } from 'vue'
  
  
  
  const users = createListResource({
  doctype: 'User',
  fields: ['name', 'first_name'],
  limit: 100,
  
  })
  users.reload()
  </script>