<template>
    <div id="habitGraphicsSecondApp">
        <div class="row w-100 m-0 mt-4 d-flex justify-content-center">
            <div class="graphic col-md-6">
                <div class="text-center">
                    <h2>Ay Analizi</h2>
                </div>                      
                <div>
                    <canvas id="monthChart" class="" width="200" height="110"></canvas>
                </div>
            </div>
            <div class="graphic col-md-6">
                <div class="text-center">
                    <h2>Hafta Analizi</h2>
                </div>                      
                <div>
                    <canvas id="weekChart" class="" width="200" height="110"></canvas>
                </div>
            </div>                
        </div>
    </div>
</template>

<script>
export default {
    props: ['theHabit'],
    computed: {
        weekScoreDataset(){
            if (this.theHabit){
                let habitDays = this.theHabit.days;
                let habitDaysCount = parseInt(habitDays.length / 7);
                let habitDaysDataset = [];
                habitDays.map((day) => {
                    habitDaysDataset.push(day.quantity);
                });
                let habitWeeksDataset = [];
                let habitWeeksLabels = [];
                for (let index = 1; index <= habitDaysCount; index++){
                    habitWeeksDataset.push(habitDaysDataset.splice(0, 7));
                    habitWeeksLabels.push(`${index}.hafta`);
                }

                let weekScoreDataset = [];
                
                habitWeeksDataset.map((week) => {
                    let totalWeekQuantity = 0;
                    week.map((dayQuantity) => {
                        totalWeekQuantity += dayQuantity;
                    });
                    weekScoreDataset.push(totalWeekQuantity);
                })
                return [weekScoreDataset, habitWeeksLabels]
            }            
        },
        monthScoreDataset(){
            if (this.theHabit){
                let habitDays = this.theHabit.days;
                let habitDaysCount = parseInt(habitDays.length / 30);
                let habitDaysDataset = [];
                habitDays.map((day) => {
                    habitDaysDataset.push(day.quantity);
                });
                let habitMonthsDataset = [];
                let habitMonthsLabels = [];
                for (let index = 1; index <= habitDaysCount; index++){
                    habitMonthsDataset.push(habitDaysDataset.splice(0, 30));
                    habitMonthsLabels.push(`${index}.ay`);
                }

                let monthScoreDataset = [];
                
                habitMonthsDataset.map((month) => {
                    let totalMonthQuantity = 0;
                    month.map((dayQuantity) => {
                        totalMonthQuantity += dayQuantity;
                    });
                    monthScoreDataset.push(totalMonthQuantity);
                })
                return [monthScoreDataset, habitMonthsLabels]
            }
        }
    },
    mounted(){
        let ctx_months = document.getElementById('monthChart');
        let monthChart = new Chart(ctx_months, {
            type: 'line',
            data: {
                labels: this.monthScoreDataset[1],
                datasets: [{
                    label: 'Rutin Günleri',
                    data: this.monthScoreDataset[0],
                    backgroundColor: [
                        'rgb(59, 208, 185)',
                        'black',
                    ],
                    borderColor: [
                        '#39a9bf',
                    ],
                    borderWidth: 2,
                }]
            },
        });

        let ctx_weeks = document.getElementById('weekChart');
        let weekChart = new Chart(ctx_weeks, {
            type: 'line',
            data: {
                labels: this.weekScoreDataset[1],
                datasets: [{
                    label: 'Rutin Haftaları',
                    data: this.weekScoreDataset[0],
                    backgroundColor: [
                        'rgb(59, 208, 185)',
                        'black',
                    ],
                    borderColor: [
                        '#39a9bf',
                    ],
                    borderWidth: 1,
                }]
            },
        });
    },      
    methods: {
        goToFirstGraphics(){
            this.$emit('activeHabitGraphicsComponent', 'HabitGraphicsFirst');
        }
    }
}
</script>

<style scoped>
i{
    cursor: pointer;
    position: absolute;
    top: 50%;
    left: 0.5%;
}
</style>