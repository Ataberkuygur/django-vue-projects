<template>
    <div id="habitTableApp">
        <div class="container">
            <div class="row w-100 d-flex justify-content-center m-0">
                    <h3>Günler</h3>
                    <div class="row w-100 d-flex justify-content-center">
                        <div v-if="clickedDay.clicked" class="field daily_score row w-100 m-0 mb-4 d-flex justify-content-center align-items-center">
                            <label class="mr-2 mt-2">{{clickedDay.day.day_number}}.gün için bitirilen '{{getCategoryOfTheHabit.daily_goal_type}}'</label>
                            <input 
                                @keypress.enter="finishTheHabitDayOrDont(clickedDay.day)" 
                                v-model="clickedDay.day.quantity" 
                                class="form-control w-25" 
                                type="number"
                            />
                        </div>                        
                        <div 
                            @click="showDailyScoreInput(day)"
                            class="box d-flex justify-content-center align-items-center" 
                            v-for="day in daysOfHabit" 
                            :class="{'done': day.done}"
                            :key="day.slug"
                        >
                            <div>{{day.day_number}}</div>
                        </div>
                    </div>                               
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'habitTableApp',
    props : ['theHabit'],
    data(){
        return{
            categoryOfTheHabit: {},
            clickedDay: { clicked: false, day: {}, day_score: 0 },
        }
    },
    computed: {
        daysOfHabit(){
            if (this.theHabit){
                return this.theHabit.days;
            }
        },
        getCategoryOfTheHabit(){
            if (this.theHabit){
                let token = localStorage.getItem('Token');
                let authorization = {
                    headers: {
                        Authorization: `Token ${token}`
                    }
                };
                axios.get(`categories/${this.theHabit.category}`, authorization)
                .then(response => this.categoryOfTheHabit = response.data)
                .catch(error => console.log(error.message));
            }
            return this.categoryOfTheHabit;
        }
    },    
    methods: {
        showDailyScoreInput(day){
            this.clickedDay = { clicked: true, day: day };
        },
        finishTheHabitDayOrDont(day){
            day.quantity = parseInt(day.quantity)
            if (day.done == false){
                day.done = true;
            }
            else{
                day.done = false;
            }
            this.$store.dispatch('finishTheHabitDayOrDontAsync', day);
            this.clickedDay.clicked = false;
        },
    }    
}
</script>

<style scoped>
.box{
    width: 5%;
    height: 40px;
    border: 1px solid black;
}

.done{
    background-color: black;
    color: white;
}

.field input{
    height: 40px;
    border-radius: 30px;
    outline: 0px;
}


@media only screen and (max-width: 768px){
    .container{
        max-width: 100%;
    }
    .box{
        width: 10%;
    }
}
</style>