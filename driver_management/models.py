from django.db import models
import datetime
from user_master.models import State, City, Location, Branch, Zone
from django.utils.html import mark_safe


class AddDriver(models.Model):
    image_upload = models.ImageField(upload_to='images/%Y/%m/', default=None)

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image_upload.url}" '
                         f'width = "100" height = "100" style = "border-radius: 50%"/>')

    # General Details
    first_name = models.CharField(max_length=20, default=None)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(choices=(('M', "Male"), ('F', "Female")), max_length=10, default="M")
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=15)
    alt_mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    marital_status = models.CharField(choices=(('M', 'Married'), ('S', 'Single')),
                                      max_length=10)
    religion = models.CharField(choices=(('H', 'Hindu'), ('M', 'Muslim'),
                                         ('C', 'Christian'), ('S', 'Sikh')),
                                max_length=10)
    cast = models.CharField(choices=(('MA', 'Marathi'),
                                     ('MU', 'Muslim'), ('GU', 'Gujarati'),
                                     ('SO', 'SouthIndian'), ('PU', 'Punjabi'),
                                     ('UP', 'UP'), ('BI', 'Bihari'), ('OT', 'Other')),
                            max_length=20,
                            default='MA')
    qualification = models.CharField(choices=(('5', '5th'), ('6', '6th'), ('7', '7th'),
                                              ('8', '8th'), ('9', '9th'), ('SS', 'SSC'), ('HS', 'HSC'),
                                              ('BC', 'BCOM'), ('BS', 'BSc'), ('BE', 'BE'), ('BA', 'BA')),
                                     default="SS", max_length=10)
    driver_type = models.CharField(choices=(('Temporary', 'Temporary'), ('Permanent', 'Permanent')), default="Temporary", max_length=10)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    language = models.CharField(choices=(('HI', 'Hindi'), ('EN', 'English'), ('BH', 'Bhojpuri')), default="HI", max_length=10)

    # Address
    t_address = models.CharField(max_length=200)
    p_address = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=10)
    aggrement_expiry_date = models.DateField()

    # Licence Information
    licence_no = models.CharField(max_length=20)
    licence_issued_from = models.CharField(max_length=20)
    licence_type = models.CharField(choices=(('TR', 'LMV-TR'), ('NT', 'LMV-NT')), default="TR", max_length=10)
    date_of_issue = models.DateField()
    date_of_expiry = models.DateField()

    # Driver Screening
    present_salary = models.FloatField(null=True, blank=True)
    expected_salary = models.FloatField()
    pan_card_no = models.CharField(max_length=15, blank=True, null=True)
    aadhar_card_no = models.CharField(max_length=20)
    blood_group = models.CharField(choices=(("1", "O+"), ("2", "O-"), ("3", "A+"), ("3", "A-"), ("3", "B+"),
                                            ("3", "B-"), ("3", "AB+"), ("3", "AB-")),
                                   max_length=10)
    passport = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    passport_no = models.CharField(max_length=20, null=True, blank=True)
    heavy_vehicle = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    car_transmission = models.CharField(choices=(("1", "Manual"), ("2", "Automatic"), ("3", "Luxury")), max_length=10)
    start_doh_date = models.DateField()
    end_doh_date = models.DateField()

    # Car Details
    car_company_name = models.CharField(max_length=15)
    transmission_type = models.CharField(choices=(("1", "Manual"), ("2", "Automatic"), ("3", "Luxury")), max_length=10)
    car_type = models.CharField(choices=(("1", "SUV"), ("2", "Sedan"), ("3", "Luxury"), ("4", "Hatchback"),
                                         ("5", "MPV"), ("6", "MUV")),
                                max_length=10)
    driven_km = models.FloatField()

    # Attach Document
    driving_licence = models.FileField(upload_to='documents/%Y/%m/', default=None)
    ration_card = models.FileField(upload_to='documents/%Y/%m/', default=None, null=True, blank=True)
    pan_card = models.FileField(upload_to='documents/%Y/%m/', default=None, null=True, blank=True)
    light_bill = models.FileField(upload_to='documents/%Y/%m/', default=None, null=True, blank=True)
    aadhar_card = models.FileField(upload_to='documents/%Y/%m/', default=None, null=True, blank=True)
    home_agreement = models.FileField(upload_to='documents/%Y/%m/', default=None, null=True, blank=True)
    affidavit = models.FileField(upload_to='documents/%Y/%m/', default=None, null=True, blank=True)

    # Previous Employment details
    company_name = models.CharField(max_length=30)
    address_location = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=20)
    worked_from = models.DateField()
    worked_till = models.DateField()
    monthly_salary = models.FloatField()
    reason_for_leaving = models.CharField(max_length=30)
    car_driven = models.CharField(max_length=20)

    # Family/Neighbour history detail
    relationship = models.CharField(max_length=20)
    member_name = models.CharField(max_length=20)
    approx_age = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    education_details = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    reference = models.CharField(max_length=15)

    # Driver status update
    schedule_training = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    training_date = models.DateField()
    training_status = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    Purchase_uniform = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    scheduled_driving_test = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    driving_test_date = models.DateField()
    driving_status = models.CharField(choices=(("1", "Approve"), ("2", "Reject")), max_length=10)
    is_approval_done = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    police_verification = models.CharField(choices=(("1", "Yes"), ("2", "No")), max_length=10)
    week_off = models.CharField(choices=(("1", "Monday"), ("1", "Tuesday"), ("1", "Wednesday"),
                                         ("1", "Thursday"), ("1", "Friday"), ("1", "Saturday"), ("1", "Sunday")),
                                max_length=10)
    scheme_type = models.CharField(choices=(("1", "Platinum"), ("2", "Gold"), ("3", "Silver")), max_length=10)
    driver_status = models.CharField(choices=(("1", "Pending"), ("2", "Approved"), ("3", "Rejected"), ("4", "Suspended")),
                                     max_length=10)
    def __str__(self):
        return self.first_name
    

class ViewDriver(models.Model):
    pass


class DriverHistory(models.Model):
    pass


class ReferDriver(models.Model):
    pass


class DriverLeave(models.Model):
    pass


class DriverBalance(models.Model):
    pass

