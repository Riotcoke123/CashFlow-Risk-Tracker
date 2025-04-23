<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>CashFlow Risk Tracker</h1>
    <p>This project simulates cash flow management, focusing on identifying early deposit risks and robbery risks. The simulation tracks weekly sales, calculates early deposits, and logs days with heightened robbery risk based on defined thresholds. The results are stored in JSON format and can be visualized through generated graphs.</p>
  <h2>Features</h2>
    <ul>
        <li>Simulates weekly sales with fluctuations.</li>
        <li>Tracks daily cash deposits and flags risks for early deposits.</li>
        <li>Identifies and logs days with high robbery risks.</li>
        <li>Saves the simulation data in JSON format.</li>
        <li>Visualizes trends for robbery risks and early deposits.</li>
    </ul>
    <h2>Installation</h2>
    <p>To use this project, you need Python 3.x and the following dependencies:</p>
    <ul>
        <li><strong>matplotlib</strong> - For plotting graphs</li>
        <li><strong>json</strong> - For saving and reading simulation data</li>
        <li><strong>random</strong> - For generating fluctuated sales values</li>
    </ul>
    <p>To install the required libraries, run the following command:</p>
    <pre><code>pip install matplotlib</code></pre>
    <h2>Usage</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/Riotcoke123/CashFlow-Risk-Tracker.git</code></pre>
        <li>Navigate to the project directory:</li>
        <pre><code>cd CashFlow-Risk-Tracker</code></pre>
        <li>Run the simulation script:</li>
        <pre><code>python cash_flow_simulation.py</code></pre>
        <li>This will generate a JSON file with the simulated cash flow data.</li>
        <li>To visualize the trends of robbery risk days and early deposits, run the following commands:</li>
        <pre><code>python plot_robbery_trends.py</code></pre>
        <pre><code>python plot_early_deposit_trends.py</code></pre>
    </ol>
    <h2>Results</h2>
    <p>The simulation generates a JSON log that tracks the sales, deposits, and risks for each day of the simulation. The logs are then used to visualize trends in:</p>
    <ul>
        <li><strong>Robbery risk days</strong> - Days where early deposits exceed robbery risk thresholds.</li>
        <li><strong>Early deposits</strong> - Total early deposits made each week.</li>
    </ul>
    <h2>Plug in Your Own Numbers</h2>
    <p>To tailor the simulation to your specific needs, simply plug in your own sales figures and risk thresholds. This flexible system allows you to simulate various scenarios by adjusting values such as:</p>
    <ul>
        <li><strong>Base Sales</strong> - Modify the sales for each day of the week to reflect real-world variations or projections.</li>
        <li><strong>Register Start Cash</strong> - Adjust the initial cash in the registers to match your operational model.</li>
        <li><strong>Early Deposit Thresholds</strong> - Tweak the thresholds that trigger early deposits and robbery risk warnings to suit different risk profiles.</li>
    </ul>
    <p>This adaptability empowers you to conduct robust scenario analysis, helping you anticipate and mitigate risks in your cash flow operations.</p>
    <h2>Example Output</h2>
    <p>The generated JSON file will contain logs in the following structure:</p>
    <pre><code>
{
    "simulation_weeks": 10,
    "weekly_logs": [
        {
            "week": 1,
            "days": {
                "Monday": {
                    "sales": 300,
                    "early_deposit": 210,
                    "night_deposit": 80,
                    "risk_flag": true,
                    "robbery_risk": false
                },
                "Tuesday": {
                    "sales": 330,
                    "early_deposit": 220,
                    "night_deposit": 90,
                    "risk_flag": true,
                    "robbery_risk": true
                },
                // more days
            },
            "week_total_deposited": 1000.5,
            "week_total_early": 600.2
        },
        // more weeks
    ],
    "totals": {
        "total_deposited": 10000.5,
        "total_early": 5000.25,
        "robbery_days": [
            {"week": 1, "day": "Tuesday"},
            // more robbery days
        ]
    }
}
    </code></pre>
    <h2>Contributions</h2>
    <p>Feel free to fork the project and submit pull requests. Contributions are welcome to improve the simulation logic, add more features, or enhance data visualization.</p>
    <h2>License</h2>
    <p>This project is licensed under the <strong>GNU General Public License v3.0</strong> - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
