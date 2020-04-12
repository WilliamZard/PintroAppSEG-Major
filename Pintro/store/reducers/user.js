 
import {
    CREATE_USER,
    GETUSER,
    UPDATE_STORY,
    UPDATE_EXPERIENCE,
    UPDATE_PASSIONS,
    UPDATE_HELP_OTHERS,
    OTHERUSER

} from '../actions/user';
const initialState = {
    Industry: "Tech",
    current_Company: "Google",
    academic_Level: "PHD",
    years_in_industry: "3",
    education: "KCL",
    email: "moin@meister.de",
    full_name: "Max",
    gender: "NA",
    help_others: ["Accounting"],
    job_title: "CEO",
    location: "London",
    passions: ["Accounting"],
    phone: "2222222",
    preferred_name: "Maxi",
    previous_Company: "Facebook",
    profile_image: "'b '",
    story: "great story"

};

export default (state = initialState, action) => {
    switch (action.type) {
        case CREATE_USER:
            return {
                Industry: action.IndustryToGet,
                current_Company: action.current_CompanyToGet,
                academic_Level: action.academic_LevelToGet,
                years_in_industry: action.years_in_industryToGet,
                education: action.educationToGet,
                email: action.emailToGet,
                full_name: action.full_nameToGet,
                gender: action.genderToGet,
                help_others: action.help_othersToGet,
                job_title: action.job_titleToGet,
                location: action.locationToGet,
                passions: action.passionsToGet,
                phone: action.phoneToGet,
                preferred_name: action.preferred_nameToGet,
                previous_Company: action.previous_CompanyToGet,
                profile_image: action.profile_imageToGet,
                story: action.storyToGet,
            }
        case UPDATE_STORY:
            return {
                Industry: action.IndustryToGet,
                current_Company: action.current_CompanyToGet,
                academic_Level: action.academic_LevelToGet,
                years_in_industry: action.years_in_industryToGet,
                education: action.educationToGet,
                email: action.emailToGet,
                full_name: action.full_nameToGet,
                gender: action.genderToGet,
                help_others: action.help_othersToGet,
                job_title: action.job_titleToGet,
                location: action.locationToGet,
                passions: action.passionsToGet,
                phone: action.phoneToGet,
                preferred_name: action.preferred_nameToGet,
                previous_Company: action.previous_CompanyToGet,
                profile_image: action.profile_imageToGet,
                story: action.storyToGet,
            }
        case UPDATE_EXPERIENCE:
            return {
                years_in_industry: action.years_in_industryToGet,
                Industry: action.IndustryToGet,
                previous_Company: action.previous_CompanyToGet,
                education: action.educationToGet,
                academic_Level: action.academic_LevelToGet,
            }
        case UPDATE_PASSIONS:
            return {
                passions: action.passionsToGet,
            }
        case UPDATE_HELP_OTHERS:
            return {
                help_others: action.help_othersToGet,
            }
        case GETUSER :
                return{
                    userObj: action.userObj
                }
        case OTHERUSER:
            return{
                otherUserObj: action.otherUserObj
            };    
            default:
                return state;
  
    }
    
};
