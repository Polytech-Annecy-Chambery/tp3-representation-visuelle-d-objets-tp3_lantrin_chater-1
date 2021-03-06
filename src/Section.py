# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:31:06 2021

@author: lantrins
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017
@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        #definir les sommets
        self.vertices = [
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [0,self.parameters['thickness'],0],
           
                [0,self.parameters['thickness'],self.parameters['height']],
                
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],0]
                
                ]
        self.faces = [
                # d??finir ici les faces
                [0, 3, 2, 1],
                [5, 6, 7, 4],
                [1, 0, 4, 5],
                
                [4, 0, 3, 7],
                [7, 3, 2, 6],
                [6, 2, 1, 5]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        return (self.parameters['height']>=x.getParameter('height')+x.getParameter('position')[2]-self.parameters['position'][2]
                and x.getParameter('position')[2]>=self.parameters['position'][2]
                and self.parameters['width']>=x.getParameter('width')+x.getParameter('position')[0]-self.parameters['position'][0]
                and x.getParameter('position')[0]>=self.parameters['position'][0]
                )    
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compl??ter en rempla??ant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
        # A compl??ter en rempla??ant pass par votre code
        gl.glPushMatrix()
        gl.glTranslatef(self.setParameters['position'][0],self.setParameters['position'][1],self.setParameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) # on trace les arrets : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv([self.parameters['color'][0]*0.3,self.parameters['color'][1]*0.3,self.parameters['color'][2]*0.3]) 
        for i in self.faces:          
            for j in i:
                gl.glVertex3fv(self.vertices[j])
        gl.glEnd()
        gl.glPopMatrix()

    # Draws the faces

    def draw(self):
        # A compl??ter en rempla??ant pass par votre code
        if self.parameters['edges']:
            self.drawEdges()
        
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv(self.parameters['color']) 
        for i in self.faces:
            for j in i:
                gl.glVertex3fv(self.vertices[j])
            
        gl.glEnd()
        gl.glPopMatrix()
            
    
            
        
  