export interface GootyVillage {
  id: number;
  name: string;
  teluguName: string;
  distanceFromHubKm: string;
  activeFarmingFamilies: number;
  primaryCrops: string[];
  soilType: string;
  aggregationCenter: string;
}

export const GOOTY_VILLAGES: GootyVillage[] = [
  { id: 1, name: "Gooty Rural", teluguName: "గుత్తి రూరల్", distanceFromHubKm: "0 km (Hub Base)", activeFarmingFamilies: 340, primaryCrops: ["Sona Masoori Paddy", "Groundnut", "Toor Dal"], soilType: "Red Sandy Loam & Black Cotton", aggregationCenter: "ONSFC Central Hub, NH-44" },
  { id: 2, name: "Basinepalle", teluguName: "బసినేపల్లి", distanceFromHubKm: "4.5 km", activeFarmingFamilies: 210, primaryCrops: ["Groundnut", "Desi Bengal Gram", "Castor"], soilType: "Red Gravelly Soil", aggregationCenter: "Basinepalle Panchayat Shed" },
  { id: 3, name: "Brahmana Palle", teluguName: "బ్రాహ్మణపల్లి", distanceFromHubKm: "6.0 km", activeFarmingFamilies: 185, primaryCrops: ["Sona Masoori Rice", "Toor Dal", "Yellow Maize"], soilType: "Clay Loam & Canal Irrigated", aggregationCenter: "Brahmana Palle Rythu Bharosa Kendra" },
  { id: 4, name: "Dharmapuram", teluguName: "ధర్మాపురం", distanceFromHubKm: "8.2 km", activeFarmingFamilies: 240, primaryCrops: ["Bold Groundnut", "Teja Red Chilies", "Jowar"], soilType: "Deep Red Loamy Soil", aggregationCenter: "Dharmapuram Old School Yard" },
  { id: 5, name: "Engilibanda", teluguName: "ఎంగిలిబండ", distanceFromHubKm: "5.8 km", activeFarmingFamilies: 165, primaryCrops: ["Kapas (Cotton)", "Bengal Gram", "Toor Dal"], soilType: "Black Cotton Soil", aggregationCenter: "Engilibanda Cross Weighbridge" },
  { id: 6, name: "Isurallapalle", teluguName: "ఈసురాళ్ళపల్లి", distanceFromHubKm: "9.5 km", activeFarmingFamilies: 195, primaryCrops: ["Sona Masoori Paddy", "Broken Rice Raw", "Pulses"], soilType: "Alluvial Canal Fringe", aggregationCenter: "Isurallapalle Rythu Seva Center" },
  { id: 7, name: "Jakkalacheruvu", teluguName: "జక్కలచెరువు", distanceFromHubKm: "11.0 km", activeFarmingFamilies: 280, primaryCrops: ["Bold Groundnut", "Red Chilies", "Castor"], soilType: "Red Sandy Clay", aggregationCenter: "Jakkalacheruvu Tank Bund Yard" },
  { id: 8, name: "Karadikonda", teluguName: "కరడికొండ", distanceFromHubKm: "13.5 km", activeFarmingFamilies: 225, primaryCrops: ["Raw Cotton (Kapas)", "Maize", "Bengal Gram"], soilType: "Deep Black Cotton Soil", aggregationCenter: "Karadikonda Temple Square" },
  { id: 9, name: "Konganapalle", teluguName: "కొంగనపల్లి", distanceFromHubKm: "12.0 km", activeFarmingFamilies: 190, primaryCrops: ["Sona Masoori Paddy", "Toor Dal", "Foxtail Korra"], soilType: "Red Loam with Wells", aggregationCenter: "Konganapalle Primary Yard" },
  { id: 10, name: "Kothapeta", teluguName: "కొత్తపేట", distanceFromHubKm: "3.2 km", activeFarmingFamilies: 310, primaryCrops: ["Groundnut", "Sona Masoori Rice", "Urad Dal"], soilType: "Red Sandy Loam", aggregationCenter: "Kothapeta NH-44 Toll Link" },
  { id: 11, name: "Mamudur", teluguName: "మాముదూరు", distanceFromHubKm: "14.0 km", activeFarmingFamilies: 260, primaryCrops: ["Desi Bengal Gram", "Cotton Bales", "Jowar"], soilType: "Deep Black Regur Soil", aggregationCenter: "Mamudur Market Yard" },
  { id: 12, name: "Marikunta", teluguName: "మారికుంట", distanceFromHubKm: "10.5 km", activeFarmingFamilies: 175, primaryCrops: ["Bold Peanuts", "Yellow Corn", "Castor"], soilType: "Gravelly Red Soil", aggregationCenter: "Marikunta Water Works Ground" },
  { id: 13, name: "Nelagonda", teluguName: "నేలగొండ", distanceFromHubKm: "15.0 km", activeFarmingFamilies: 230, primaryCrops: ["Kapas (Cotton)", "Teja Red Chilies", "Toor Dal"], soilType: "Black Cotton Heavy Soil", aggregationCenter: "Nelagonda Gram Panchayat Yard" },
  { id: 14, name: "Pattikonda Road Cluster", teluguName: "పత్తికొండ రోడ్డు క్లస్టర్", distanceFromHubKm: "7.0 km", activeFarmingFamilies: 290, primaryCrops: ["Groundnut", "Sona Masoori", "Bengal Gram"], soilType: "Mixed Red & Black Soils", aggregationCenter: "Pattikonda Road Junction" },
  { id: 15, name: "Peddadoddi", teluguName: "పెద్దదొడ్డి", distanceFromHubKm: "8.5 km", activeFarmingFamilies: 320, primaryCrops: ["Paddy BPT 5204", "Unpolished Toor Dal", "Groundnut"], soilType: "Rich Loamy Soil", aggregationCenter: "Peddadoddi Community Hall" },
  { id: 16, name: "Pothulapadu", teluguName: "పోతులపాడు", distanceFromHubKm: "11.5 km", activeFarmingFamilies: 180, primaryCrops: ["Desi Bengal Gram", "Yellow Maize", "Cotton"], soilType: "Black Cotton Soil", aggregationCenter: "Pothulapadu Rythu Mandali" },
  { id: 17, name: "Rajapuram", teluguName: "రాజాపురం", distanceFromHubKm: "6.5 km", activeFarmingFamilies: 215, primaryCrops: ["Bold Groundnut", "Foxtail Millet (Korra)", "Castor"], soilType: "Red Soil with Drip Irrigation", aggregationCenter: "Rajapuram Center Point" },
  { id: 18, name: "Ramapuram", teluguName: "రామాపురం", distanceFromHubKm: "4.8 km", activeFarmingFamilies: 250, primaryCrops: ["Sona Masoori Rice", "Toor Dal", "Idli Broken Rice"], soilType: "Red Sandy Loam", aggregationCenter: "Ramapuram Rythu Sangham" },
  { id: 19, name: "Thondapadu", teluguName: "తొండపాడు", distanceFromHubKm: "16.0 km", activeFarmingFamilies: 205, primaryCrops: ["Cotton Bales", "Desi Chana", "Jowar"], soilType: "Deep Black Cotton Soil", aggregationCenter: "Thondapadu Cooperative Yard" },
  { id: 20, name: "Turkapalle", teluguName: "తురకపల్లి", distanceFromHubKm: "12.5 km", activeFarmingFamilies: 170, primaryCrops: ["Groundnut Pods", "Teja Chilies", "Maize"], soilType: "Red Gravel Loam", aggregationCenter: "Turkapalle Main Street" },
  { id: 21, name: "Ubicherla", teluguName: "ఉబిచర్ల", distanceFromHubKm: "10.0 km", activeFarmingFamilies: 220, primaryCrops: ["Sona Masoori", "Bold Groundnut", "Urad Dal"], soilType: "Loamy Red Clay", aggregationCenter: "Ubicherla Bus Stand Yard" },
  { id: 22, name: "Vadiampeta", teluguName: "వడియంపేట", distanceFromHubKm: "7.8 km", activeFarmingFamilies: 245, primaryCrops: ["Desi Bengal Gram", "Toor Dal", "Red Chilies"], soilType: "Mixed Black Soil", aggregationCenter: "Vadiampeta Weighbridge Yard" },
  { id: 23, name: "Venkatampalle", teluguName: "వెంకటంపల్లి", distanceFromHubKm: "9.0 km", activeFarmingFamilies: 190, primaryCrops: ["Groundnut", "Foxtail Korra", "Castor"], soilType: "Red Sandy Soil", aggregationCenter: "Venkatampalle Panchayat Office" },
  { id: 24, name: "Yerraguntla", teluguName: "ఎర్రగుంట్ల", distanceFromHubKm: "13.0 km", activeFarmingFamilies: 270, primaryCrops: ["Kapas (Cotton)", "Bengal Gram", "Toor Dal"], soilType: "Heavy Black Regur Soil", aggregationCenter: "Yerraguntla Agro Sourcing Yard" }
];
