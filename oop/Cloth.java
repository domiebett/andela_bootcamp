/*Basic Cloth class for use in Boutiques and Cloth shops
contains trouser*/

class Cloth {
    protected String material, color, designer;
    
    public String getMaterial(){
        return material;
    }
    public void setMaterial(String material){
        this.material = material;
    }
    
    public String getColor(){
        return color;
    }
    public void setColor(String color){
        this.color = color;
    }
    
    public String getDesigner(){
        return designer;
    }
    public void setDesigner(String designer){
        this.designer = designer;
    }
    
}

class Trouser extends Cloth{
    private int waist_size, height;
    private String name, description, designer;
    private final int number_of_legs = 2;

    Trouser(){
        
    }
    
    Trouser(String material, String designer){
        this.material = material;
        
        if (material.equals("Denim")){
            this.name = "Jeans";
            this.description = "Best for casual events";
        }
        else if (material.equals("Cotton")){
            this.name = "Office Pants";
            this.description = "Best for Official events";
        }
        else if (material.equals("Khaki")){
            this.name = "Khaki Pants";
            this.description = "Multipurpose trousers";
        }
        
    }
    
    public int getNumber_of_legs() {
        return number_of_legs;
    }

    public int getWaist_size() {
        return waist_size;
    }

    public void setWaist_size(int waist_size) {
        this.waist_size = waist_size;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }   

}

class Shirt extends Cloth{
    private int number_of_arms,length;
    private String size;
    
    Shirt(){
        
    }
    
    Shirt(String material){
        this.material = material;
    }

    public int getNumber_of_arms() {
        return number_of_arms;
    }

    public void setNumber_of_arms(int number_of_arms) {
        this.number_of_arms = number_of_arms;
    }

    public int getLength() {
        return length;
    }

    public void setLenth(int length) {
        this.length = length;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
}