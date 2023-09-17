from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car

class CarModel:
    @staticmethod
    def Calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def Glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def Palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def Rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear)
        return Car(engine, battery, tires)
    
    @staticmethod
    def Thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        return Car(engine, battery, tires)
