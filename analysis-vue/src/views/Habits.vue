<template>
    <div id="habitsApp">
        <component 
            :is="activeComponent" 
            @activeComponent="activeComponent = $event" 
            v-bind:activeComponent="activeComponent"
            v-bind:habitSlug="habitSlug"
            @habitSlug="habitSlug = $event"
            v-bind:userId="userId" 
        />
    </div>
</template>

<script>
import HabitList from '../components/Habits/HabitList.vue'
import SingleHabit from '../components/Habits/SingleHabit.vue'
export default {
    name: 'habitsApp',
    data(){
        return{
            userId: this.$route.params.id,
            activeComponent: 'HabitList',
            habitSlug: '',
        }
    },
    components: {
        HabitList,
        SingleHabit,
    }
}
</script>

<style scoped>

</style>