class PersonalityProfile:
    def __init__(self, name, zodiac_sign, favorite_color, age, gender, energy):
        self.name = name
        self.zodiac_sign = zodiac_sign
        self.favorite_color = favorite_color
        self.age = age
        self.gender = gender
        self.energy = energy
        self.profile = self.create_personality_profile()
    
    def create_personality_profile(self):
        profile = {}
        
        # Example rules for personality traits based on inputs
        profile['fashion_personality'] = self.determine_fashion_personality()
        profile['personality_avatar'] = self.determine_personality_avatar()
        profile['best_career_fit'] = self.determine_best_career_fit()
        
        return profile
    
    def determine_fashion_personality(self):
        if self.favorite_color.lower() in ['red', 'black']:
            return 'Bold and Edgy'
        elif self.favorite_color.lower() in ['blue', 'green']:
            return 'Calm and Relaxed'
        else:
            return 'Eclectic and Unique'
    
    def determine_personality_avatar(self):
        if self.zodiac_sign.lower() in ['leo', 'aries', 'sagittarius']:
            return 'The Leader'
        elif self.zodiac_sign.lower() in ['virgo', 'capricorn', 'taurus']:
            return 'The Perfectionist'
        else:
            return 'The Dreamer'
    
    def determine_best_career_fit(self):
        if self.age < 30:
            return 'Creative Fields'
        else:
            return 'Leadership Roles'
