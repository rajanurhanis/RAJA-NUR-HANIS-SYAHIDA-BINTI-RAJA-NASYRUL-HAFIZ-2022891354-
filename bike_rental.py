import tkinter as tk
import mysql.connector

#Connecting to the MySQL database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bike_rental"
) 

#Creating a cursor object to execute SQL queries
mycursor = mydb.cursor()

#Function to handle the calculation and database saving
def collect_data():
    bike_type = package_var.get()
    hour = int(hours_entry.get())

    #The prices below are to defined the value from the user selections
    prices = {
        "Comfort bike": 5,
        "Kids' bike": 5,
        "E-bike": 10,
        "Recumbent bike": 6,
    }

    #Calculating the total price which derived from the selection. (Bike type, Hour).
    total_price = (prices[bike_type] * hour)

    #Inserting data to the database (using 3 attributes).
    sql = "INSERT INTO `rental` (Package_type, Package_hour, Package_price) VALUES (%s,%s, %s)"
    val = (bike_type, hour, total_price)
    mycursor.execute (sql, val)
    mydb.commit()

    #Printing back the output. 
    output_label.config (text=f"Bike type : {bike_type}, Hour : {hour}, Total Price: RM{total_price}")

#Main window
root = tk.Tk()
root.title("Bike Rental")
root.geometry('400x600')

#Page title
label = tk.Label(root, text= 'Choose your bike !', font = ("Times New Roman", "16", "bold"))
label.pack (ipadx = 10, ipady = 10)

#Prices list
prices_text = tk.Text (root, height = 15, width = 45)
prices_text.pack (pady = 20)

#Defining list using pricebox
prices_text.insert (tk.END, "Types of bike and prices per hour: \n\n")
prices_text.insert (tk.END, "Comfort bike: \nRM5 per hour\n\n")
prices_text.insert (tk.END, "Kids' bike: \nRM5 per hour\n\n")
prices_text.insert (tk.END, "E-bike: \nRM10 per hour\n\n")
prices_text.insert (tk.END, "Recumbent bike: \nRM6 per hour\n\n")
prices_text.configure (state = 'disabled')

#Bike rental system dropdown (label)
hours_label = tk.Label (root, text = "Choose your bike")
hours_label.pack()

#Bike type dropdown
package_var = tk.StringVar (root)
package_var.set ("Select your bike") #default value before selection
bike_dropdown = tk.OptionMenu (root, package_var, "Comfort bike", "Kids' bike", "E-bike", "Recumbent bike")
bike_dropdown.pack (pady=10)

#Hour entry. In this section, label and user can enter data through entry.
hours_label = tk.Label (root, text = "Hour: ")
hours_label.pack ()
hours_entry = tk.Entry (root)
hours_entry.pack ()

#Save button
save_button = tk.Button (root, text= "Total", command = collect_data)
save_button.pack ()

#Output label & result
label = tk.Label (root, text = "Your order detail:", font = ("Times New Romans", 12))
label.pack (ipadx = 10, ipady = 10)
output_label = tk.Label (root, text = "")
output_label.pack ()

#Setting the background colour
root.configure(bg ='#355E3B')

root.mainloop()