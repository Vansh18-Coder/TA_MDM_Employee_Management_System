const form = document.getElementById("employeeForm");


// Add employee
form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const employee = {

        employee_id:
            document.getElementById("employee_id").value,

        name:
            document.getElementById("name").value,

        department:
            document.getElementById("department").value,

        designation:
            document.getElementById("designation").value,

        salary:
            document.getElementById("salary").value,

        contact:
            document.getElementById("contact").value
    };


    const response = await fetch("/employees", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(employee)
    });


    const result = await response.json();

    alert(result.message || result.error);

    form.reset();

    loadEmployees();

});


// Load employees
async function loadEmployees() {

    const response = await fetch("/employees");

    const employees = await response.json();

    displayEmployees(employees);
}


// Search employees
async function searchEmployees() {

    const keyword =
        document.getElementById("search").value;

    const response =
        await fetch(
            "/employees/search?keyword=" +
            encodeURIComponent(keyword)
        );

    const employees = await response.json();

    displayEmployees(employees);
}


// Display employees
function displayEmployees(employees) {

    const list =
        document.getElementById("employeeList");

    list.innerHTML = "";


    employees.forEach(function(employee) {

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>${employee.id}</td>

            <td>${employee.employee_id}</td>

            <td>${employee.name}</td>

            <td>${employee.department}</td>

            <td>${employee.designation}</td>

            <td>${employee.salary}</td>

            <td>${employee.contact}</td>

            <td>

                <button onclick="updateEmployee(${employee.id})">
                    Update
                </button>

                <button onclick="deleteEmployee(${employee.id})">
                    Delete
                </button>

            </td>
        `;

        list.appendChild(row);

    });
}


// Delete employee
async function deleteEmployee(id) {

    if (!confirm("Delete this employee?")) {
        return;
    }

    const response =
        await fetch("/employees/" + id, {

            method: "DELETE"
        });


    const result = await response.json();

    alert(result.message || result.error);

    loadEmployees();
}


// Update employee
async function updateEmployee(id) {

    const name =
        prompt("Enter new name:");

    if (!name) {
        return;
    }


    const department =
        prompt("Enter new department:");

    const designation =
        prompt("Enter new designation:");

    const salary =
        prompt("Enter new salary:");

    const contact =
        prompt("Enter new contact:");


    const response =
        await fetch("/employees/" + id, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                employee_id: prompt("Enter Employee ID:"),

                name: name,

                department: department,

                designation: designation,

                salary: salary,

                contact: contact

            })
        });


    const result = await response.json();

    alert(result.message || result.error);

    loadEmployees();
}


// Load employees when page opens
loadEmployees();