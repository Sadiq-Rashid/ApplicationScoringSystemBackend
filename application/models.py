from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Application(models.Model):


    GENDER = (
        ('Male', "Male"),
        ('Female', "Female"),
        ("Other", "Other")
    )

    EDUCATION_LEVEL = (
        ('Primary level', "Primary level"),
        ('Secondary level', 'Secondary level'),
        ('Tartiary level', 'Tartiary level')
    )

    COMPANY_EXISTENCE = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    BUSINESS_STAGE = (
        ('Start up', 'Start up'),
        ('Growth', 'Growth'),
        ('Marturity', 'Marturity'),
        ('Renewal', 'Renewal'),
        ('Decline', 'Descline')
    )

    EMPLOYMENT_STATUS = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Self-employed', 'Self-employed')
    )

    APPLICANT_SUITS = (
        ('start up', 'start up'),
        ('company founder', 'company founder'),
        ('employer', 'employer'),
        ('other', 'other')
    )


    id = models.AutoField(primary_key=True)	
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    fullName = models.CharField(max_length=250)
    registrationDate = models.DateField()
    dateOfBirth = models.DateField()
    phoneNumber = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER)
    country = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100, choices=EDUCATION_LEVEL)
    graduationDate =  models.DateField()
    employmentStatus = models.CharField(max_length=100, choices=EMPLOYMENT_STATUS)
    experienceYears = models.PositiveBigIntegerField()
    doYouHaveCompany = models.CharField(max_length=50, choices=COMPANY_EXISTENCE)
    yourBusinessName = models.CharField(max_length=250, default="N/A")
    yourBusinessStage = models.CharField(max_length=250, choices=BUSINESS_STAGE, default="N/A")
    DateOfYourBusinessEstablishment  = models.DateField()
    totalFoundersInYourBusiness = models.PositiveSmallIntegerField(default=None)
    whatBestSuitsYou = models.CharField(max_length=200, choices=APPLICANT_SUITS)


    # Innovation & Disruption
    ideaDescription = models.TextField()
    problemIdentification = models.TextField()
    solutionApproach = models.TextField()
    differentiationAndUSP = models.TextField()
    prototypeStage = models.TextField()


    # Scalability and marketing
    primaryCustomerBaseDefinition = models.TextField()
    industryOperateIn = models.TextField()
    keyChallengesExpectation = models.TextField()
    competitorsListAndReasons = models.TextField()

    # Business Model Viability
    mainBusinessWins = models.TextField()
    acceleratorOrIncubatorDetails = models.TextField()


    # Financial Projections 
    currentRevenueGeneration = models.TextField()
    fundingReceivedAmountAED = models.TextField()
    prizeMoneyUsagePlan = models.TextField()


    # Team Competence
    emiratizationRateOfFoundingTeam = models.TextField()
    foundersAndLeadershipExperienceReview = models.TextField()
    mentorSupportingBusiness = models.TextField()
    businessOperationsLocation = models.TextField()







    def __str__(self):
        return self.fullName
  
