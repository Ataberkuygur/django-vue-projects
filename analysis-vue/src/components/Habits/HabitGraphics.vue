<template>
    <div id="habitGraphicsApp">
        <component
            :is="activeHabitGraphicsComponent"
            @activeHabitGraphicsComponent="activeHabitGraphicsComponent = $event"
            :theHabit="theHabit"
        />
    </div>
</template>

<script>
import HabitGraphicsFirst from './HabitGraphicsFirst.vue'
import HabitGraphicsSecond from './HabitGraphicsSecond.vue'
export default {
    props: ['theHabit'],
    data(){
        return{
            activeHabitGraphicsComponent: 'HabitGraphicsFirst',
        }
    }, 
    components: {
        HabitGraphicsFirst,
        HabitGraphicsSecond,
    } 
}
</script>

<style scoped>

</style>