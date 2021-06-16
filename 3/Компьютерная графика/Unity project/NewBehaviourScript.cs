using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public struct MoleculaPath
{
    public static string ASP = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\ASP.pdb";
    public static string ALA = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\ALA.pdb";
    public static string ARG = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\ARG.pdb";
    public static string ASN = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\ASN.pdb";
    public static string CYS = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\CYS.pdb";
    public static string GLN = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\GLN.pdb";
    public static string GLU = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\GLU.pdb";
    public static string GLY = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\GLY.pdb";
    public static string HIS = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\HIS.pdb";
    public static string ILE = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\ILE.pdb";
    public static string LEU = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\LEU.pdb";
    public static string LYS = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\LYS.pdb";
    public static string MET = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\MET.pdb";
    public static string PHE = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\PHE.pdb";
    public static string PRO = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\PRO.pdb";
    public static string SER = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\SER.pdb";
    public static string THR = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\THR.pdb";
    public static string TRP = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\TRP.pdb";
    public static string TYR = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\TYR.pdb";
    public static string VAL = "C:\\Users\\grish\\Documents\\Unity\\New Unity Project\\Assets\\aminoacids\\VAL.pdb";
}


public class CAtom
    {
        public string stringname;   // 01-06 "ATOM"
        public int number;          // 07-11 atom serial number
        public string atomname;     // 13-16 atom name
        public char altLoc;         // 17    alternate location indicator
        public string residue;      // 18-20 residue name
        public string chain_id;     // 22    chain ID
        public int nresidue;        // 23-26 residue sequence number
        public char iCode;          // 27    code for insertion of residues 
        public float x;             // 31-38 coord x
        public float y;             // 39-46 coord y
        public float z;             // 47-54 coord z
        public float occupancy;     // 55-60 occupancy
        public float temp;          // 61-66 temperature factor
        public string symbol;       // 77-78 symbol
        public string charge;       // 79-80 charge of the atom
    }

class Parser
{
    private static void SetAtom(string line, List<CAtom> atomList)
    {
        CAtom atom = new CAtom();
        atom.stringname = line.Substring(0, 6).Trim();
        atom.number = Convert.ToInt32(line.Substring(6, 5).Trim());
        atom.atomname = line.Substring(12, 4).Trim();
        atom.altLoc = line.Substring(16, 1)[0];
        atom.residue = line.Substring(17, 3).Trim();
        atom.chain_id = line.Substring(21, 1).Trim();
        atom.nresidue = Convert.ToInt32(line.Substring(22, 4).Trim());
        atom.iCode = line.Substring(26, 1)[0];
        atom.x = (float)Convert.ToDouble(line.Substring(30, 8).Trim().Replace(".", ",")); 
        atom.y = (float)Convert.ToDouble(line.Substring(38, 8).Trim().Replace(".", ","));
        atom.z = (float)Convert.ToDouble(line.Substring(46, 8).Trim().Replace(".", ","));
        atom.occupancy = (float)Convert.ToDouble(line.Substring(54, 6).Trim().Replace(".", ","));
        atom.temp = (float)Convert.ToDouble(line.Substring(60, 6).Trim().Replace(".", ","));
        atom.symbol = line.Substring(76, 2);
        atom.charge = " 0";

        atomList.Add(atom);

    }
    public static int Parse(string path, List<CAtom> atomList)
    {
        string line;
        int atomCounter = 0;
        try
        {
            StreamReader sr = new StreamReader(path);
            line = sr.ReadLine();
            while (line != null)
            {
                if(line.IndexOf("ATOM") == 0)
                {
                    SetAtom(line, atomList);
                    atomCounter++;
                }

                line = sr.ReadLine();
            }
            sr.Close();
        }
        catch {Debug.Log("read file error");}

        return atomCounter;
    } 
}



public class NewBehaviourScript : MonoBehaviour
{   
    public Transform panel;
    public GameObject handleAtoms;
    private List<CAtom> atomList = new List<CAtom>();
    void OnGUI() 
    {
        int width = 40;
        int height = 20;
        if(GUI.Button(new Rect(0, 0, width, height), "ALA")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.ALA);
        }
        if(GUI.Button(new Rect(0, height+1, width, height), "ARG")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.ARG);
        }
        if(GUI.Button(new Rect(0, 2*height+1, width, height), "ASN")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.ASN);
        }
        if(GUI.Button(new Rect(0, 3*height+1, width, height), "ASP")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.ASP);
        }
        if(GUI.Button(new Rect(0, 4*height+1, width, height), "CYS")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.CYS);
        }
        if(GUI.Button(new Rect(0, 5*height+1, width, height), "GLN")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.GLN);
        }
        if(GUI.Button(new Rect(0, 6*height+1, width, height), "GLU")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.GLU);
        }
        if(GUI.Button(new Rect(0, 7*height+1, width, height), "GLY")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.GLY);
        }
        if(GUI.Button(new Rect(0, 8*height+1, width, height), "HIS")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.HIS);
        }
        if(GUI.Button(new Rect(0, 9*height+1, width, height), "ILE")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.ILE);
        }
        if(GUI.Button(new Rect(0, 10*height+1, width, height), "LEU")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.LEU);
        }
        if(GUI.Button(new Rect(0, 11*height+1, width, height), "LYS")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.LYS);
        }
        if(GUI.Button(new Rect(0, 12*height+1, width, height), "MET")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.MET);
        }
        if(GUI.Button(new Rect(0, 13*height+1, width, height), "PHE")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.PHE);
        }
        if(GUI.Button(new Rect(0, 14*height+1, width, height), "PRO")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.PRO);
        }
        if(GUI.Button(new Rect(0, 15*height+1, width, height), "SER")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.SER);
        }
        if(GUI.Button(new Rect(0, 16*height+1, width, height), "THR")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.THR);
        }
        if(GUI.Button(new Rect(0, 17*height+1, width, height), "TRP")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.TRP);
        }
        if(GUI.Button(new Rect(0, 18*height+1, width, height), "TYR")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.TYR);
        }
        if(GUI.Button(new Rect(0, 19*height+1, width, height), "VAL")){
            ClearMolecula();
            LoadMolecula(MoleculaPath.VAL);
        }
        
    }

    void LoadMolecula(string path)
    {
        handleAtoms = new GameObject();
        int cnt = Parser.Parse(path, atomList);
        int ordinalNum = 0;
        GameObject [] sphere = new GameObject[cnt];
        
        foreach (CAtom atom in atomList)
            { 
                sphere[ordinalNum] = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                    sphere[ordinalNum].name = atom.atomname;
                    sphere[ordinalNum].transform.position = new Vector3(atom.x, atom.y, atom.z);
                    SetSphereColor(sphere[ordinalNum], atom);
                    SetSphereRadius(sphere[ordinalNum], atom);
                    sphere[ordinalNum].transform.parent = handleAtoms.transform;
                ordinalNum++;
            }
        
    }
    void ClearMolecula()
    {
        atomList.Clear();
        Destroy(handleAtoms);
    }

    public void SetSphereColor(GameObject sphere, CAtom atom)
    {
        Color color = Color.white;
        float k = 0.25f;
        string strColor = atom.symbol.Trim();

        switch (strColor)
        {
            case "O": color = Color.Lerp(Color.red, Color.grey, k); break;
            case "N": color = Color.Lerp(Color.blue, Color.grey, k); break;
            case "C": color = Color.Lerp(Color.black, Color.grey, k * 2f); break;
            case "H": color = Color.Lerp(Color.white, Color.grey, k); break;
            default:
                color = Color.Lerp(Color.green, Color.green, k); break;
        }

        Renderer rend = sphere.GetComponent<Renderer>();
        rend.material.shader = Shader.Find("Standard");
        rend.material.color = color;

    }
    public void SetSphereRadius(GameObject sphere, CAtom atom)
    {
        float radius;
        string strName = atom.symbol.Trim();
        float koef = 1.5f;
        switch (strName)
        {
            case "O": radius = 0.529f * koef; break;
            case "N": radius = 0.71f * koef; break;
            case "C": radius = 0.76f * koef; break;
            case "H": radius = 0.46f * koef; break;
            default: radius = 1; break;
        }
        sphere.transform.localScale = new Vector3(radius, radius, radius);

    }
    // Start is called before the first frame update
    void Start()
    {
       LoadMolecula(MoleculaPath.ASP);
    }
    public float speed = 0f;
    public Vector3 euler = new Vector3(0, 0, 0);
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.DownArrow)){ euler.x = euler.x + 1; }
        if(Input.GetKeyUp(KeyCode.DownArrow)) { euler.x = euler.x - 1; }

        if(Input.GetKeyDown(KeyCode.UpArrow)){ euler.x = euler.x - 1; }
        if(Input.GetKeyUp(KeyCode.UpArrow)){ euler.x = euler.x + 1; }

        if(Input.GetKeyDown(KeyCode.LeftArrow)){ euler.y = euler.y + 1; }
        if(Input.GetKeyUp(KeyCode.LeftArrow)){ euler.y = euler.y - 1; }
        
        if(Input.GetKeyDown(KeyCode.RightArrow)){ euler.y = euler.y - 1; }
        if(Input.GetKeyUp(KeyCode.RightArrow)){ euler.y = euler.y + 1; }


        if(Input.GetMouseButtonDown(1))
        {
            speed = 4f;
        }
        if(Input.GetMouseButtonUp(1))
        {
            speed = 0f;
        }
        handleAtoms.transform.Rotate(Vector3.left, Input.GetAxis("Mouse Y") * speed);
        handleAtoms.transform.Rotate(Vector3.down, Input.GetAxis("Mouse X") * speed);
        handleAtoms.transform.Translate(0, 0, Input.GetAxis("Mouse ScrollWheel"));
        handleAtoms.transform.Rotate(euler);

    }

}
