class User {
    constructor(
        id,
        name,
        email,
        phone,
        currentJobTitle,
        currentCompany,
        story,
        workExperience,
        industry,
        education,
        academicLevel,
        passionTags,
        profilePicture
    ) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.currentJobTitle = currentJobTitle;
        this.currentCompany = currentCompany;
        this.story = story;
        this.workExperience = workExperience;
        this.industry = industry;
        this.education = education;
        this.academicLevel = academicLevel;
        this.passionTags = passionTags;
        this.profilePicture = profilePicture;

    }



    get getId() {
        return this.id;
    }
    get getName() {
        return this.name;
    }
    get getEmail() {
        return this.email;
    }
    get getPhone() {
        return this.phone;
    }
    get getCurrentJobTitle() {
        return this.currentCompany;
    }
    get getCurrentCompany() {
        return this.currentCompany;
    }
    get getStory() {
        return this.story;
    }
    get getWorkExperience() {
        return this.workExperience;
    }
    get getIndustry() {
        return this.industry;
    }
    get getEducation() {
        return this.education;
    }
    get setAcademicLevel() {
        return this.academicLevel;
    }
    get setPassionTags() {
        return this.passionTags;
    }
    get setProfilePicture() {
        return this.profilePicture;
    }
    set setId(id) {
        this.id = id;
    }
    set setName(name) {
        this.name = name;
    }
    set setEmail(email) {
        this.email = email;
    }
    set setPhone(phome) {
        this.phone = phone;
    }
    set setCurrentJobTitle(currentJobTitle) {
        this.currentJobTitle = currentJobTitle;
    }
    set setCurrentCompany(currentCompany) {
        this.currentCompany = currentCompany;
    }
    set setStory(story) {
        this.story = story;
    }
    set setWorkExperience(workExperience) {
        this.workExperience = workExperience;
    }
    set setIndustry(industry) {
        this.industry = industry;
    }
    set setEducation(education) {
        this.education = education;
    }
    set setAcademicLevel(academicLevel) {
        this.academicLevel = academicLevel;
    }
    set setPassionTags(passionTags) {
        this.passionTags = passionTags;
    }
    set setProfilePicture(profilePicture) {
        this.profilePicture = profilePicture;
    }






}
export default User;