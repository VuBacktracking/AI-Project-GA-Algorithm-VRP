import matplotlib.pyplot as plt
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6 import QtCore
import folium

def drawMap(tourmanager, best_path):
    for city in tourmanager:
        plt.plot(city.getLongitude(), city.getLatitude(), "ro")
        plt.annotate(city.getID(), (city.getLongitude(), city.getLatitude()))

    for i in range(len(best_path)):
        try:
            first = best_path[i]
            second = best_path[i + 1]

            plt.plot([first.getLongitude(), second.getLongitude()], [first.getLatitude(), second.getLatitude()], "gray")
        except:
            continue

    # first = best_path[0]
    # second = best_path[-1]
    # plt.plot([first.getLongitude(), second.getLongitude()], [first.getLatitude(), second.getLatitude()], "gray")

    plt.show()

class HCMMapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bản đồ Thành Phố Hồ Chí Minh')
        self.setGeometry(400, 100, 800, 600)

        self.map = folium.Map(zoom_start=10, location=[10.7674978, 106.6363691])
        self.map_widget = QWebEngineView(self)
        self.map_widget.setHtml(self.map._repr_html_())
        self.setCentralWidget(self.map_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.map_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def draw(self, best_path):
        for cityIndex in range(len(best_path)):
            if cityIndex == 0 or cityIndex == len(best_path)-1:
                folium.Marker(
                    location=best_path.get_city(cityIndex).get_coordinates(),
                    popup=best_path.get_city(cityIndex).name,
                    icon=folium.Icon(color='red', icon='exclamation-circle', prefix='fa')
                ).add_to(self.map)
            else:
                folium.Marker(
                    location=best_path.get_city(cityIndex).get_coordinates(),
                    popup=best_path.get_city(cityIndex).name,
                    icon=folium.Icon(color='blue', icon='exclamation-circle', prefix='fa')
                ).add_to(self.map)

        path_coords = [city.get_coordinates() for city in best_path]
        folium.PolyLine(locations=path_coords, color='red', weight=2.5).add_to(self.map)

        start_coords = best_path.get_city(0).get_coordinates()
        end_coords = best_path.get_city(len(best_path) - 1).get_coordinates()
        folium.PolyLine(locations=[start_coords, end_coords], color='red', weight=2.5).add_to(self.map)

        self.map_widget.setHtml(self.map._repr_html_())
