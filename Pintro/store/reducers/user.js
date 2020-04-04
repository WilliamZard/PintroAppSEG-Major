import { 
    CREATE_USER 
    } from '../actions/user';
    const initialState = {
        full_name:null,
        preferrred_name:null,
        profile_image:null,
        short_bio:null,
        gender:null,
        story:null,
        email:null,
        phone_number:null,
        current_Company:null,
        years_in_industry:null,
        Industry:null,
        previous_Company:null,
        previous_Company_Year_Finished:null,
        university:null,
        university_Year_Finished:null,
        academic_Level:null,
        location:null,
        passions:null,
        help_Others:null,
        
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case CREATE_USER:
                return {
                    full_name:action.full_nameTP,
                    preferrred_name:action.preferrred_nameTP,
                    profile_image:action.profile_imageTP,
                    short_bio:action.short_bioTP,
                    gender:action.genderTP,
                    story:action.storyTP,
                    email:action.emailTP,
                    phone_number:action.phone_numberTP,
                    current_Company:action.current_CompanyTP,
                    years_in_industry:action.years_in_industryTP,
                    Industry:action.IndustryTP,
                    previous_Company:action.previous_CompanyTP,
                    previous_Company_Year_Finished:action.previous_Company_Year_FinishedTP,
                    university:action.universityTP,
                    university_Year_Finished:action.university_Year_FinishedTP,
                    academic_Level:action.academic_LevelTP,
                    location:action.locationTP,
                    passions:action.passionsTP,
                    help_Others:action.help_OthersTP,
                    
                };
        }
        return state;
    };