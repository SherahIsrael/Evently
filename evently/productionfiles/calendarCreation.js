document.addEventListener('DOMContentLoaded', function() {
    // Generate year and month
    const today = new Date();
    const currentYear = today.getFullYear();
    const currentMonth = today.getMonth() + 1;
    const monthName = new Intl.DateTimeFormat('en-US', { month: 'long' }).format(today);
    document.getElementById('currentMonth').textContent = monthName;
    document.getElementById('currentYear').textContent = currentYear;


    function loadCalendar(year, month) {
        fetch(`/events_json/${year}/${month}/`)
            .then(response => response.json())
            .then(events => {
                const calendarBody = document.getElementById('calendar-body');
                calendarBody.innerHTML = '';
                const cal = generateCalendar(year, month);
                cal.forEach(week => {
                    const row = document.createElement('tr');
                    week.forEach(day => {
                        const cell = document.createElement('td');
                        cell.classList.add('event-day');
                        if (day) {
                            cell.textContent = day;
                            const event = events.find(event => event.day === day);
                            if (event) {
                                const dot = document.createElement('div');
                                dot.classList.add('event-dot');
                                cell.appendChild(dot);
                            }
                        }
                        row.appendChild(cell);
                    });
                    calendarBody.appendChild(row);
                });
            });
    }

    function generateCalendar(year, month) {
        const cal = [];
        const firstDay = new Date(year, month - 1, 1).getDay();
        const lastDate = new Date(year, month, 0).getDate();
        let week = new Array(7).fill(null);

        for (let day = 1; day <= lastDate; day++) {
            const date = new Date(year, month - 1, day);
            const dayOfWeek = (date.getDay() + 6) % 7;  // Adjust to start week from Monday
            week[dayOfWeek] = day;
            if (dayOfWeek === 6 || day === lastDate) {
                cal.push(week);
                week = new Array(7).fill(null);
            }
        }
        return cal;
    }

    loadCalendar(currentYear, currentMonth);
});