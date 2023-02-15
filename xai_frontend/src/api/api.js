import axiosInstance from './index'
import qs from 'qs'

const axios = axiosInstance

export const getRanking = () => {return axios.get(`http://localhost:8000/api/getranking`)}

export const postRanking = (userRanking, ThirdRanking) => {
    // userRanking;
    // ThirdRanking;
    // return new Promise(res => {
    //     res
    // })
    return axios.get(`http://localhost:8000/api/compareranking`,
 { params: {'user_ranking': JSON.stringify(userRanking), 'third_ranking': JSON.stringify(ThirdRanking)},
    paramsSerializer: params => {
        return qs.stringify(params)
    }
})
}
export const getShap = () => {return axios.get('http://localhost:8000/api/shap')}
export const getPreference = () => {return axios.get('http://localhost:8000/api/userpreference')}