
from application.models import Application
from rest_framework import serializers
from django.contrib.auth.models import User


class ApplicationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)	
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    email = serializers.EmailField()
    fullName = serializers.CharField()
    registrationDate = serializers.DateField()
    dateOfBirth = serializers.DateField()
    phoneNumber = serializers.CharField()
    gender = serializers.CharField()
    country = serializers.CharField()
    education_level = serializers.CharField()
    graduationDate =  serializers.DateField()
    employmentStatus = serializers.CharField()
    experienceYears = serializers.IntegerField()
    doYouHaveCompany = serializers.CharField()
    yourBusinessName = serializers.CharField()
    yourBusinessStage = serializers.CharField()
    DateOfYourBusinessEstablishment  = serializers.DateField()
    totalFoundersInYourBusiness = serializers.IntegerField()
    whatBestSuitsYou = serializers.CharField()

    # Innovation & Disruption
    ideaDescription = serializers.CharField()
    problemIdentification = serializers.CharField()
    solutionApproach = serializers.CharField()
    differentiationAndUSP = serializers.CharField()
    prototypeStage = serializers.CharField()


    # Scalability and marketing
    primaryCustomerBaseDefinition = serializers.CharField()
    industryOperateIn = serializers.CharField()
    keyChallengesExpectation = serializers.CharField()
    competitorsListAndReasons = serializers.CharField()

    # Business Model Viability
    mainBusinessWins = serializers.CharField()
    acceleratorOrIncubatorDetails = serializers.CharField()


    # Financial Projections 
    currentRevenueGeneration = serializers.CharField()
    fundingReceivedAmountAED = serializers.CharField()
    prizeMoneyUsagePlan = serializers.CharField()


    # Team Competence
    emiratizationRateOfFoundingTeam = serializers.CharField()
    foundersAndLeadershipExperienceReview = serializers.CharField()
    mentorSupportingBusiness = serializers.CharField()
    businessOperationsLocation = serializers.CharField()


    def create(self, validated_data):
            """
            create and return application given validated data
            """
            return Application.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
            """
            Update and return an existing Application instance given validated data.
            """
            instance.email = validated_data.get('email', instance.email)
            instance.fullName = validated_data.get('fullName', instance.fullName)
            instance.registrationDate = validated_data.get('registrationDate', instance.registrationDate)
            instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
            instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
            instance.gender = validated_data.get('gender', instance.gender)
            instance.country = validated_data.get('country', instance.country)
            instance.education_level = validated_data.get('education_level', instance.education_level)
            instance.graduationDate = validated_data.get('graduationDate', instance.graduationDate)
            instance.employmentStatus = validated_data.get('employmentStatus', instance.employmentStatus)
            instance.experienceYears = validated_data.get('experienceYears', instance.experienceYears)
            instance.doYouHaveCompany = validated_data.get('doYouHaveCompany', instance.doYouHaveCompany)
            instance.yourBusinessName = validated_data.get('yourBusinessName', instance.yourBusinessName)
            instance.yourBusinessStage = validated_data.get('yourBusinessStage', instance.yourBusinessStage)
            instance.DateOfYourBusinessEstablishment = validated_data.get('DateOfYourBusinessEstablishment', instance.DateOfYourBusinessEstablishment)
            instance.totalFoundersInYourBusiness = validated_data.get('totalFoundersInYourBusiness', instance.totalFoundersInYourBusiness)
            instance.whatBestSuitsYou = validated_data.get('whatBestSuitsYou', instance.whatBestSuitsYou)

            instance.ideaDescription = validated_data.get('ideaDescription', instance.ideaDescription)
            instance.problemIdentification = validated_data.get('problemIdentification', instance.problemIdentification)
            instance.solutionApproach = validated_data.get('solutionApproach', instance.solutionApproach)
            instance.differentiationAndUSP = validated_data.get('differentiationAndUSP', instance.differentiationAndUSP)
            instance.prototypeStage = validated_data.get('prototypeStage', instance.prototypeStage)

        # Scalability and marketing
            instance.primaryCustomerBaseDefinition = validated_data.get('primaryCustomerBaseDefinition', instance.primaryCustomerBaseDefinition)
            instance.industryOperateIn = validated_data.get('industryOperateIn', instance.industryOperateIn)
            instance.keyChallengesExpectation = validated_data.get('keyChallengesExpectation', instance.keyChallengesExpectation)
            instance.competitorsListAndReasons = validated_data.get('competitorsListAndReasons', instance.competitorsListAndReasons)
    
            # Business Model Viability
            instance.mainBusinessWins = validated_data.get('mainBusinessWins', instance.mainBusinessWins)
            instance.acceleratorOrIncubatorDetails = validated_data.get('acceleratorOrIncubatorDetails', instance.acceleratorOrIncubatorDetails)
    
            # Financial Projections 
            instance.currentRevenueGeneration = validated_data.get('currentRevenueGeneration', instance.currentRevenueGeneration)
            instance.fundingReceivedAmountAED = validated_data.get('fundingReceivedAmountAED', instance.fundingReceivedAmountAED)
            instance.prizeMoneyUsagePlan = validated_data.get('prizeMoneyUsagePlan', instance.prizeMoneyUsagePlan)
    
            # Team Competence
            instance.emiratizationRateOfFoundingTeam = validated_data.get('emiratizationRateOfFoundingTeam', instance.emiratizationRateOfFoundingTeam)
            instance.foundersAndLeadershipExperienceReview = validated_data.get('foundersAndLeadershipExperienceReview', instance.foundersAndLeadershipExperienceReview)
            instance.mentorSupportingBusiness = validated_data.get('mentorSupportingBusiness', instance.mentorSupportingBusiness)
            instance.businessOperationsLocation = validated_data.get('businessOperationsLocation', instance.businessOperationsLocation)

            
            instance.save()
            return instance
