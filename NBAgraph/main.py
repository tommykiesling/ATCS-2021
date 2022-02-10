import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import seaborn

# Apply the default theme
sns.color_palette("Paired")

# Load an example dataset
df = pd.read_csv("Salaries.csv")

# Create a visualization
#sns.relplot(
   #data=df,
   #x="Total Salary", y="Wins",
#)
#plt.text(x=136623929,y=44.6, s="MIL", color ='green')
#plt.text(x=118804016,y=39.6, s="ATL", color ='red')
#plt.text(x=128858241,y=49.6, s="PHX", color ='orange')
#plt.text(x=171105334,y=37.6, s="GSW", color ='yellow')
#plt.text(x=95774839,y=20.6, s="OKC", color ='blue')

sns.relplot(
   data=df,
   x="Salary Rank", y="Team Placement"

)
#plt.text(x=136623929,y=4.87, s="MIL", color ='green')
#plt.text(x=118804016,y=1.44, s="ATL", color ='red')
#plt.text(x=128858241,y=4.97, s="PHX", color ='orange')
#plt.text(x=171105334,y=.4, s="GSW", color ='yellow')
#plt.text(x=95774839,y=-10.83, s="OKC", color ='blue')

plt.show()

