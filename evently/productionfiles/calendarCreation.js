document.addEventListener("DOMContentLoaded", function() {
    // Calendar Creation
    const today = new Date();
    let currentYear = today.getFullYear();
    let currentMonth = today.getMonth();

    function updateCalendar(year, month) {
        const monthName = new Intl.DateTimeFormat("en-US", { month: "long" }).format(new Date(year, month));
        document.getElementById("currentMonth").textContent = monthName;
        document.getElementById("currentYear").textContent = year;

        fetch(`/events_json/${year}/${month + 1}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(events => {
                const calendarBody = document.getElementById("calendarBody");
                calendarBody.innerHTML = '';
                const firstDayOfMonth = new Date(year, month, 1).getDay();
                const daysInMonth = new Date(year, month + 1, 0).getDate();
                const daysInPreviousMonth = new Date(year, month, 0).getDate();

                let date = 1;
                let prevMonthDate = daysInPreviousMonth - (firstDayOfMonth - 1);

                // Generate the rows for the calendar
                for (let i = 0; i < 6; i++) {
                    const row = document.createElement("tr");

                    // Generate the cells for each day in the week
                    for (let j = 0; j < 7; j++) {
                        const cell = document.createElement("td");
                        if (i === 0 && j < firstDayOfMonth) {
                            // Previous month's days
                            cell.textContent = prevMonthDate;
                            cell.classList.add("otherMonth");
                            prevMonthDate++;
                        } else if (date > daysInMonth) {
                            // Next month's days
                            cell.textContent = date - daysInMonth;
                            cell.classList.add("otherMonth");
                            date++;
                        } else {
                            // Current month's days
                            cell.textContent = date;
                            cell.classList.add("dayHover");
                            cell.addEventListener('click', function() {
                                displayEvents(year, month + 1, date, events.filter(event => event.day === date));
                            });
                            const event = events.find(event => event.day === date);
                            if (event) {
                                const dot = document.createElement("div");
                                dot.classList.add("eventDot");
                                cell.appendChild(dot);
                            }
                            date++;
                        }
                        row.appendChild(cell);
                    }
                    calendarBody.appendChild(row);
                }
            })
            .catch(error => {
                console.error("There has been a problem with your fetch operation:", error);
            });
    }
    
    function displayEvents(events) {
        const eventsList = document.getElementById("eventList");
        eventsList.innerHTML = "";

        if (events.length === 0) {
            eventsList.innerHTML = "<li>No events</li>";
        } else {
            events.forEach(event => {
                const listItem = document.createElement("li");
                listItem.textContent = event.name;
                eventsList.appendChild(listItem);
            });
        }
    }

    // Update Calendar
    document.getElementById("prevMonth").addEventListener("click", function() {
        if (currentMonth === 0) {
            currentMonth = 11;
            currentYear--;
        } else {
            currentMonth--;
        }
        updateCalendar(currentYear, currentMonth);
    });

    document.getElementById("nextMonth").addEventListener("click", function() {
        if (currentMonth === 11) {
            currentMonth = 0;
            currentYear++;
        } else {
            currentMonth++;
        }
        updateCalendar(currentYear, currentMonth);
    });

    updateCalendar(currentYear, currentMonth);

    // Sign In Modal 
    document.getElementById("signInBtn").addEventListener("click", function() {
        signInModal.style.display = "block";
    })
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
      signInModal.style.display = "none";
    }

    // Sign Up Modal 
    document.getElementById("signUpBtn").addEventListener("click", function() {
        signUpModal.style.display = "block";
    })
    var span = document.getElementsByClassName("close")[1];
    span.onclick = function() {
      signUpModal.style.display = "none";
    }
});