$(document).ready(function() {

    function loadDashboardData() {
        $.getJSON('/api/dashboard-data', function(data) {
            $('#total-income').text('$' + data.total_income);
            $('#total-expense').text('$' + data.total_expense);
            $('#balance').text('$' + data.balance);

            // Transactions Table
            const tbody = $('.transactions-table tbody');
            tbody.empty();
            data.transactions.forEach(function(t) {
                tbody.append(`
                    <tr>
                        <td>${t.date}</td>
                        <td>${t.category}</td>
                        <td>${t.amount}</td>
                        <td>${t.description}</td>
                    </tr>
                `);
            });

            // Bar chart
            const maxValue = data.total_income + data.total_expense; // Commensurate
            const incomeBarHeight = (data.total_income / maxValue) * 150;  // 150px max height
            const expenseBarHeight = (data.total_expense / maxValue) * 150;

            $('.income-bar').animate({ height: incomeBarHeight + 'px' }, 600);
            $('.expense-bar').animate({ height: expenseBarHeight + 'px' }, 600);
        });
    }

    loadDashboardData();
});
