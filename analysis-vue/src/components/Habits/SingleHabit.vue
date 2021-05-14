<template>
    <div id="singleHabitApp">
        <div class="row w-100 d-flex align-items-center justify-content-end m-0">
            <i @click="goBack" class="fa fa-arrow-left fa-lg text-dark mr-4 mt-3"></i>
        </div>        
        <div class="container">
            <div class="row w-100 d-flex justify-content-between m-0 mt-2">
                <div class="button-group">
                    <button @click="goToTable" class="button button-ocean-blue text-white component-button">Takvim</button>
                </div>
                <div class="button-group">
                    <button @click="goToGraphics" class="button button-ocean-blue text-white component-button">Grafikler</button>
                </div>
            </div>
        </div>
        <component 
            :is="activeHabitComponent" 
            :theHabit="getTheHabit"
        >
        </component>
    </div>
</template>

<script>
import HabitTable from './HabitTable.vue'
import HabitGraphics from './HabitGraphics.vue'
export default {
    name: 'singleHabitApp',   
    props: ['activeComponent'],
    data(){
        return{
            theHabit: null,
            activeHabitComponent: 'HabitTable',
        }
    },
    computed: {
        getTheHabit(){
            if (!this.theHabit){
                return this.$store.getters.getTheHabit;
            }
        },
    },
    methods: {
        goToTable(){
            this.activeHabitComponent = 'HabitTable';
        },
        goToGraphics(){
            this.activeHabitComponent = 'HabitGraphics';
        },
        goBack(){
            this.$emit('activeComponent', 'HabitList');
        }        
    },
    components: {
        HabitTable,
        HabitGraphics,
    }
}
</script>

<style scoped>
.component-button{
    width: 100px;
    height: 40px;
    outline: 0px;
}

i{
    cursor: pointer;
}

@media only screen and (max-width: 768px){
    i{
        top: 12%;
        right: 2%;
        font-size: 1.1em;
    }
}
</style>