import { 
    CREATE_USER,
    GETUSER 
    } from '../actions/user';
    const initialState = {
        full_name:"Ronald Koeman",
        preferrred_name:"Ron",
        profile_image:"",
        short_bio:"interesting bio",
        gender:"male",
        story:"story goes here",
        email:"ronald@kcl.com",
        phone_number:"314123213",
        current_Company:"MC",
        years_in_industry:"23",
        Industry:"Health",
        previous_Company:"KCL",
        previous_Company_Year_Finished:"2019",
        university:"KCL",
        university_Year_Finished:"2019",
        academic_Level:"PHD",
        location:"London",
        passions:["Accounting"],
        help_Others:["Accounting"],
        
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
            case GETUSER :
                return{
                    userObj: action.userObj
                };    
        }
        return state;
    };