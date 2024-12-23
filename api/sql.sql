-- Create a new database
CREATE DATABASE IF NOT EXISTS SugarcaneDiseases;

-- Use the newly created database
USE SugarcaneDiseases;

-- Create a table to store disease information
CREATE TABLE IF NOT EXISTS disease_info (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique ID for each disease record
    disease_name VARCHAR(255) NOT NULL,        -- Name of the disease
    symptoms TEXT,                             -- Symptoms of the disease
    pathogen TEXT,                             -- Pathogen responsible for the disease
    cause TEXT,                                -- Cause of the disease
    favourable_conditions TEXT,                -- Favourable conditions for the disease
    disease_cycle TEXT,                        -- Disease cycle
    pre_management TEXT,                       -- Pre-planting management strategies
    mid_management TEXT,                       -- Mid-planting management strategies
    future_management TEXT,                    -- Future management strategies
    precautions TEXT                          -- Precautions for the disease
);

-- Insert sample data into the disease_info table
INSERT INTO disease_info (disease_name, symptoms, pathogen, cause, favourable_conditions, disease_cycle, pre_management, mid_management, future_management, precautions)
VALUES

('Healthy', 
 'Plants show no signs of disease, robust growth.', 
 'N/A', 
 'N/A', 
 'Optimal growing conditions.', 
 'N/A', 
 'Ensure soil health through proper nutrient management, Use disease-free and robust planting material.', 
 'Maintain optimal growing conditions (water, nutrients, and pest control), Regularly monitor for any signs of disease.', 
 'Continue using resistant varieties and improve soil health practices, Implement integrated pest management strategies.', 
 'N/A'),

('Mosaic', 
 'Chlorotic or yellowish stripes on the basal portion of the younger foliage, leading to stunted and chlorotic plants.', 
 'Sugarcane mosaic potyvirus', 
 'Viral infection transmitted by aphids.', 
 'Presence of aphid vectors and infected setts.', 
 'Primary spread through infected canes used as seed.', 
 'Use disease-free planting material to prevent viral infection, Select resistant varieties if available.', 
 'Monitor for aphid populations and apply insecticides as needed, Rogue out infected plants immediately to prevent spread.', 
 'Rotate with non-host crops to disrupt the virus cycle, Continue to develop and plant resistant varieties.', 
 'Rogue out the diseased clumps periodically.'),


('Red Rot', 
 'The first external symptom appears mostly on third or fourth leaf which withers away at the tips along the margins.', 
 'Colletotrichum falcatum', 
 'Fungal infection causing internal rot of the stem.', 
 'Monoculturing of sugarcane and waterlogged conditions .', 
 'The fungus is sett-borne and persists in the soil on diseased clumps.', 
 'Select disease-free planting material and use resistant varieties, Treat setts with fungicides before planting.', 
 'Monitor fields for symptoms and apply fungicides as needed, Maintain proper irrigation and drainage.', 
 'Practice crop rotation with non-host plants, Regularly scout for disease and remove infected plants.', 
 'Avoid ratooning of the diseased crop.'),

('Rust', 
 'Minute, elongated, yellow spots appear on both surfaces of young leaves, turning brown on maturity.', 
 'Puccinia erianthi', 
 'Fungal infection caused by rust spores.', 
 'High humidity and warm temperatures.', 
 'The fungus survives on collateral hosts and infected stubbles.', 
 'Remove collateral hosts from the area before planting, Use disease-resistant varieties.', 
 'Monitor for symptoms and apply fungicides as necessary, Ensure proper spacing and air circulation between plants.', 
 'Practice crop rotation to break the disease cycle, Implement integrated pest management strategies.', 
 'Regularly inspect crops for early signs of infection.'),
 

('Yellow (Leaf Scald)', 
 'Whitish lines appear on the leaves, run to the full length of leaves and sheaths.', 
 'Xanthomonas albilineans', 
 'Bacterial infection causing leaf lesions.', 
 'Poor drainage and high humidity.', 
 'The bacterium remains viable in the soil and infected canes.', 
 'Select disease-free planting material, Use healthy setts from disease-resistant varieties.', 
 'Monitor for symptoms and apply appropriate fungicides, Maintain proper irrigation.', 
 'Practice crop rotation with non-host plants, Regularly scout for disease and remove infected plants.', 
 'Remove infected plants immediately, Practice field sanitation.');
 
 
 SET SQL_SAFE_UPDATES = 1;
Select * from disease_info;
-- Add a new column for disease description
ALTER TABLE disease_info
ADD COLUMN description TEXT;

-- Update the table with the disease descriptions
UPDATE disease_info
SET description = 'Yellow Disease is a viral infection, often caused by Sugarcane Yellow Leaf Syndrome (SCYLS), transmitted by aphids. It results in yellowing of the leaves and a reduction in cane yield.'
WHERE disease_name = 'Yellow';

UPDATE disease_info
SET description = 'Mosaic disease is caused by a complex of viruses, typically Sugarcane Mosaic Virus (SCMV). It affects the plant’s leaves, causing a mosaic-like appearance and reduced yield.'
WHERE disease_name = 'Mosaic';

UPDATE disease_info
SET description = 'Healthy sugarcane is free from any disease or pest. It exhibits optimal growth and high sugar content.'
WHERE disease_name = 'Healthy';

UPDATE disease_info
SET  description = 'RedRot is a fungal disease caused by Colletotrichum falcatum, affecting the sugarcane stalk. It causes internal decay and discoloration, which leads to weakening of the plant.'
WHERE disease_name = 'Red Rot';

UPDATE disease_info
SET description = 'Rust is caused by the fungus Puccinia melanocephala. It primarily affects the leaves of sugarcane, causing rust-colored pustules.'
WHERE disease_name = 'Rust';


UPDATE disease_info
SET disease_name = 'RedRot' -- is a fungal disease caused by Colletotrichum falcatum, affecting the sugarcane stalk. It causes internal decay and discoloration, which leads to weakening of the plant.'
WHERE disease_name = 'Red Rot';




