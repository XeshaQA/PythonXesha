class Doctor:
    def treat(self):
        print('Врач проводит осмотр пациента')

class Surgeon(Doctor):
    def treat(self):
        print('Хирург проводит операцию')
class Dentist(Doctor):
    def treat(self):
        print('Стоматолог лечит зубы')

class Therapist(Doctor):
    def treat(self):
        print('Терапевт назначает лечение')

    def assign_doctor(self, patient):

        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()
        print(f'Пациенту назначен врач: {patient.doctor.__class__.__name__}')

class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


print('Пациент #1 - план лечение')

patient1 = Patient(treatment_plan=1)
therapist = Therapist()
therapist.assign_doctor(patient1)
patient1.doctor.treat()

print('Пациент #2 - план лечения')
patient2 = Patient(treatment_plan=2)
therapist.assign_doctor(patient2)
patient2.doctor.treat()

print('Пациент #3 - план лечения')
patient3 = Patient(treatment_plan=3)
therapist.assign_doctor(patient3)
patient3.doctor.treat()
