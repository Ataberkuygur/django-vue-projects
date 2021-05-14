<template>
    <div id="habitGraphicsApp">
        <div class="row w-100 d-flex justify-content-center">
            <h1>Grafikler</h1>
            <div class="row w-100 m-0 mt-4 d-flex justify-content-center">
                <div class="graphic col-md-3">
                    <div class="text-center">
                        <h2>Kalan Gün Analizi</h2>
                    </div>                    
                    <div>
                        <canvas id="dayChart" class="" width="200" height="100"></canvas>
                    </div>
                </div>
                <div class="graphic col-md-3">
                    <div class="text-center">
                        <h2>Kalan Hafta Analizi</h2>
                    </div>                    
                    <div>
                        <canvas id="weekChart" class="" width="200" height="200"></canvas>
                    </div>
                </div>
                <div class="graphic col-md-3">
                    <div class="text-center">
                        <h2>Kalan Ay Analizi</h2>
                    </div>                    
                    <div>
                        <canvas id="monthChart" class="" width="200" height="200"></canvas>
                    </div>
                </div>
                <i @click="goToSecondGraphics" class="fa fa-arrow-right fa-lg text-dark mr-4 mt-3"></i>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['theHabit'],
    computed: {
        dayDataset(){
            if (this.theHabit){
                let habitDays = this.theHabit.days;
                let doneDays = habitDays.filter((day) => {
                    if (day.done == true){
                        return true;
                    }
                });
                let notDoneDays = habitDays.filter((day) => {
                    if (day.done == false){
                        return true;
                    }
                });
                let dataset = [doneDays.length, notDoneDays.length];
                return dataset;                
            }
        },
        weekDataset(){
            if (this.theHabit){
                let habitDays = this.theHabit.days;
                let doneDays = habitDays.filter((day) => {
                    if (day.done == true){
                        return true;
                    }
                });
                let doneWeeks = parseInt(doneDays.length / 7)
                let notDoneDays = habitDays.filter((day) => {
                    if (day.done == false){
                        return true;
                    }
                });
                let notDoneWeeks = parseInt(notDoneDays.length / 7)
                let dataset = [doneWeeks, notDoneWeeks];
                return dataset;                
            }
        },
        monthDataset(){
            if (this.theHabit){
                let habitDays = this.theHabit.days;
                let doneDays = habitDays.filter((day) => {
                    if (day.done == true){
                        return true;
                    }
                });
                let doneWeeks = parseInt(doneDays.length / 30)
                let notDoneDays = habitDays.filter((day) => {
                    if (day.done == false){
                        return true;
                    }
                });
                let notDoneWeeks = parseInt(notDoneDays.length / 30)
                let dataset = [doneWeeks, notDoneWeeks];
                return dataset;                
            }
        },
    },
    mounted(){
        let ctx_days = document.getElementById('dayChart');
        let dayChart = new Chart(ctx_days, {
            type: 'pie',
            data: {
                labels: ['Biten Gün', 'Kalan Gün'],
                datasets: [{
                    label: 'Rutin Günleri',
                    data: [this.dayDataset[0], this.dayDataset[1]],
                    backgroundColor: [
                        'rgb(59, 208, 185)',
                        'black',
                    ],
                    borderColor: [
                        '#39a9bf',
                    ],
                    borderWidth: 3,
                }]
            },
        });

        let ctx_weeks = document.getElementById('weekChart');
        let weekChart = new Chart(ctx_weeks, {
            type: 'pie',
            data: {
                labels: ['Biten Hafta', 'Kalan Hafta'],
                datasets: [{
                    label: 'Rutin Haftaları',
                    data: [this.weekDataset[0], this.weekDataset[1]],
                    backgroundColor: [
                        'rgb(59, 208, 185)',
                        'black',
                    ],
                    borderColor: [
                        '#39a9bf',
                    ],
                    borderWidth: 3,
                }]
            },
        });

        let ctx_months = document.getElementById('monthChart');
        let monthChart = new Chart(ctx_months, {
            type: 'pie',
            data: {
                labels: ['Biten Ay', 'Kalan Ay'],
                datasets: [{
                    label: 'Rutin Ayları',
                    data: [this.monthDataset[0], this.monthDataset[1]],
                    backgroundColor: [
                        'rgb(59, 208, 185)',
                        'black',
                    ],
                    borderColor: [
                        '#39a9bf',
                    ],
                    borderWidth: 3,
                }]
            },
        });
    },
    methods: {
        goToSecondGraphics(){
            this.$emit('activeHabitGraphicsComponent', 'HabitGraphicsSecond');
        }
    }
}
</script>

<style scoped>
.fa{
    cursor: pointer;
    position: absolute;
    top: 50%;
    right: 0.5%;
}
</style>