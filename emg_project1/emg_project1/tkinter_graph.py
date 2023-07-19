import tkinter as tk
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_emg_data(port):
    ser = serial.Serial(port)

    fig, ax = plt.subplots(figsize=(8, 4))
    max_data_points = 1000  # Set the maximum number of data points to display on the graph
    xs = [0] * max_data_points
    ys = [0] * max_data_points
    line, = ax.plot(xs, ys)

    def update_graph():
        if ser.in_waiting:
            data = ser.readline().decode('utf-8').rstrip()
            try:
                value = int(data)

                # Append new data to the end of the buffer
                xs.append(xs[-1] + 1)
                ys.append(value)

                # Discard the oldest data if the buffer size exceeds the maximum
                if len(xs) > max_data_points:
                    xs.pop(0)
                    ys.pop(0)

                # Update the data for the line
                line.set_data(xs, ys)

                # Adjust the x-axis limits to display the entire range of data
                ax.set_xlim(xs[0], xs[-1])
                ax.relim()
                ax.autoscale_view()

                # Redraw the canvas
                canvas.draw()

            except ValueError:
                pass

        root.after(1, update_graph)

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Set the window to full screen
    root.attributes('-fullscreen', True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    def close_window():
        root.destroy()
