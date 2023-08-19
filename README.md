<h1>OOP Concept Test</h1>

<p>
    This module is designed to help explorers determine if there is an impenetrable obstruction when digging to the core of the earth. It calculates the expected time for a machine to travel a certain distance and checks if the actual time exceeds the expected time by a specified threshold. If the actual time exceeds the expected time by the specified threshold, then there is an impenetrable obstruction. Otherwise, there is no impenetrable obstruction.
</p>

<h2>Usage</h2>
<h3>Installation:</h3>

No installation is required for this module as it consists of a single Python file.<br />
No external APIs, No libraries, no frameworks, pure OOP concept.
<h2>Usage:</h2>
<li> Import <code>is_impenetrable</code> function from the <code>obstruction_class</code> module into your Python script.</li>

```python
from obstruction_class import is_impenetrable
```
<h4> Provide the following parameters:</h4>
<li>expected_time: Expected time in minutes</li>
<li>actual_time: Actual time in minutes</li>

```python
if is_impenetrable(expected_time, actual_time): <br />
    print("There is an impenetrable obstruction!.")
else:
    print("There is no impenetrable obstruction.!")
```
    
<h2>Explanation:</h2>

<li>function calculates the expected time it will take to get from point a to point b by adding 60 minutes to <code>expected_time_to_reach.</code> </li>
<li>It also calculates the maximum allowed time based on the speed and distance.</li>
<li>If the <code>actual_time</code>  exceeds both the threshold time and the maximum allowed time, it indicates an impenetrable obstruction.</li>

<h2>Examples</h2>
<p>Here's an example of how to use the module:</p> 
    
```Python
from obstruction_class import is_impenetrable

speed = 10  # Speed in miles per hour
distance = 15  # Distance in miles
location_b = distance / speed * 60  # Expected time in minutes

location_a = 78  # Actual time in minutes

if is_impenetrable(location_b, location_a):
    print("There is an impenetrable obstruction!")
else:
    print("There is no impenetrable obstruction!")
```

<h2>Run the <code>main.py</code> script:</h2>
<p>Run the following command to run the <code>main.py</code> script:</p>

```Python
python main.py
```

if you are using ubuntu, run the following command:
```Python
python3 main.py
```
<h2>Note</h2>
<p>This module is designed for learning purposes and may require further enhancements for production use.</p>

<h2>Author</h2>
<p>Isah Jacob</p>
